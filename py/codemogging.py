import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import sys
import random

# ---------- CONFIG ----------
WIDTH, HEIGHT = 1000, 700
CUBE_SIZE = 0.95
ANIM_FRAMES = 15

# ---------- COLORS ----------
WHITE = (1, 1, 1)
YELLOW = (1, 1, 0)
RED = (1, 0, 0)
ORANGE = (1, 0.5, 0)
BLUE = (0, 0, 1)
GREEN = (0, 1, 0)
BLACK = (0, 0, 0)

# ---------- CAMERA ----------
camera_yaw = 45
camera_pitch = 30
camera_distance = 12
mouse_down = False

# ---------- CUBIE ----------
class Cubie:
    def __init__(self, x, y, z):
        self.pos = [x, y, z]
        self.anim_pos = [x, y, z]
        self.colors = [
            RED if x == 1 else BLACK,
            ORANGE if x == -1 else BLACK,
            WHITE if y == 1 else BLACK,
            YELLOW if y == -1 else BLACK,
            BLUE if z == 1 else BLACK,
            GREEN if z == -1 else BLACK,
        ]

cubies = []
for x in [-1, 0, 1]:
    for y in [-1, 0, 1]:
        for z in [-1, 0, 1]:
            cubies.append(Cubie(x, y, z))

# ---------- DRAW ----------
def draw_cubie(c):
    glPushMatrix()
    glTranslatef(c.anim_pos[0], c.anim_pos[1], c.anim_pos[2])
    glBegin(GL_QUADS)

    faces = [
        [(1,-1,-1),(1,1,-1),(1,1,1),(1,-1,1)],
        [(-1,-1,1),(-1,1,1),(-1,1,-1),(-1,-1,-1)],
        [(-1,1,-1),(1,1,-1),(1,1,1),(-1,1,1)],
        [(-1,-1,1),(1,-1,1),(1,-1,-1),(-1,-1,-1)],
        [(-1,-1,1),(-1,1,1),(1,1,1),(1,-1,1)],
        [(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,-1)]
    ]

    for i, verts in enumerate(faces):
        glColor3fv(c.colors[i])
        for v in verts:
            glVertex3f(v[0]*CUBE_SIZE/2, v[1]*CUBE_SIZE/2, v[2]*CUBE_SIZE/2)

    glEnd()
    glPopMatrix()

# ---------- ROTATION STATE ----------
move_queue = []
current_move = None
anim_frame = 0
move_history = []

# ---------- LOGIC ----------
def queue_move(axis, layer, clockwise, record=True):
    move_queue.append((axis, layer, clockwise, record))

def apply_rotation(axis, layer, clockwise):
    angle = math.pi / 2 * (-1 if clockwise else 1)
    sin_a = round(math.sin(angle))
    cos_a = round(math.cos(angle))

    for c in cubies:
        if c.pos["xyz".index(axis)] == layer:
            x, y, z = c.pos

            if axis == "x":
                c.pos[1], c.pos[2] = y*cos_a - z*sin_a, y*sin_a + z*cos_a
                c.colors[2], c.colors[4], c.colors[3], c.colors[5] = \
                    c.colors[4], c.colors[3], c.colors[5], c.colors[2]

            elif axis == "y":
                c.pos[0], c.pos[2] = x*cos_a + z*sin_a, -x*sin_a + z*cos_a
                c.colors[0], c.colors[4], c.colors[1], c.colors[5] = \
                    c.colors[5], c.colors[0], c.colors[4], c.colors[1]

            elif axis == "z":
                c.pos[0], c.pos[1] = x*cos_a - y*sin_a, x*sin_a + y*cos_a
                c.colors[0], c.colors[2], c.colors[1], c.colors[3] = \
                    c.colors[2], c.colors[1], c.colors[3], c.colors[0]

            c.pos = [int(round(p)) for p in c.pos]
            c.anim_pos = c.pos.copy()

# ---------- ANIMATION ----------
def update_animation():
    global current_move, anim_frame

    if not current_move and move_queue:
        current_move = move_queue.pop(0)
        anim_frame = 0

    if not current_move:
        return

    axis, layer, clockwise, record = current_move
    step = (math.pi / 2) / ANIM_FRAMES
    angle = step * (-1 if clockwise else 1)

    sin_a = math.sin(angle)
    cos_a = math.cos(angle)

    for c in cubies:
        if c.pos["xyz".index(axis)] == layer:
            x, y, z = c.anim_pos
            if axis == "x":
                c.anim_pos[1] = y*cos_a - z*sin_a
                c.anim_pos[2] = y*sin_a + z*cos_a
            elif axis == "y":
                c.anim_pos[0] = x*cos_a + z*sin_a
                c.anim_pos[2] = -x*sin_a + z*cos_a
            elif axis == "z":
                c.anim_pos[0] = x*cos_a - y*sin_a
                c.anim_pos[1] = x*sin_a + y*cos_a

    anim_frame += 1

    if anim_frame >= ANIM_FRAMES:
        apply_rotation(axis, layer, clockwise)
        if record:
            move_history.append((axis, layer, clockwise))
        current_move = None

# ---------- SCRAMBLE / SOLVE ----------
def scramble():
    move_history.clear()
    for _ in range(20):
        axis = random.choice("xyz")
        layer = random.choice([-1, 0, 1])
        cw = random.choice([True, False])
        queue_move(axis, layer, cw, True)

def solve():
    for axis, layer, cw in reversed(move_history):
        queue_move(axis, layer, not cw, False)
    move_history.clear()

# ---------- MAIN ----------
def main():
    global camera_yaw, camera_pitch, camera_distance, mouse_down

    pygame.init()
    pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Rubik's Cube – Animated")

    glEnable(GL_DEPTH_TEST)
    glViewport(0, 0, WIDTH, HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, WIDTH / HEIGHT, 0.1, 50)
    glMatrixMode(GL_MODELVIEW)

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()

            if e.type == MOUSEBUTTONDOWN:
                if e.button == 1:
                    mouse_down = True
                if e.button == 4:
                    camera_distance -= 0.5
                if e.button == 5:
                    camera_distance += 0.5

            if e.type == MOUSEBUTTONUP:
                mouse_down = False

            if e.type == MOUSEMOTION and mouse_down:
                dx, dy = e.rel
                camera_yaw += dx * 0.4
                camera_pitch += dy * 0.4

            if e.type == KEYDOWN and not current_move:
                ccw = pygame.key.get_mods() & KMOD_LSHIFT

                if e.key == K_1: queue_move("x", -1, not ccw)
                if e.key == K_2: queue_move("x",  0, not ccw)
                if e.key == K_3: queue_move("x",  1, not ccw)

                if e.key == K_q: queue_move("y", -1, not ccw)
                if e.key == K_w: queue_move("y",  0, not ccw)
                if e.key == K_e: queue_move("y",  1, not ccw)

                if e.key == K_a: queue_move("z", -1, not ccw)
                if e.key == K_s: queue_move("z",  0, not ccw)
                if e.key == K_d: queue_move("z",  1, not ccw)

                if e.key == K_f: scramble()
                if e.key == K_r: solve()

        update_animation()

        glClearColor(0.1, 0.1, 0.1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        cx = camera_distance * math.cos(math.radians(camera_pitch)) * math.sin(math.radians(camera_yaw))
        cy = camera_distance * math.sin(math.radians(camera_pitch))
        cz = camera_distance * math.cos(math.radians(camera_pitch)) * math.cos(math.radians(camera_yaw))
        gluLookAt(cx, cy, cz, 0, 0, 0, 0, 1, 0)

        for c in cubies:
            draw_cubie(c)

        pygame.display.flip()

if __name__ == "__main__":
    main()
