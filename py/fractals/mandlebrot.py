import numpy as np
from renderer import array_to_picture

def mandlebrot(c: complex, limit: int=5):
    z = 0 + 0j
    for i in range(limit):
        z = z**2 + c
        if abs(z) > 2:
            return (i / limit)
    return 1

# Example usage
if __name__ == "__main__":
    limit = 100
    vmandelbrot = np.vectorize(mandlebrot)
    width, height = 3840, 2160
    x = np.linspace(-2.0, 1.0, width)
    y = np.linspace(-1.25, 1.25, height)
    X, Y = np.meshgrid(x, y)
    C = X + (1j * Y)

    mandelbrot_vals = vmandelbrot(C, limit=limit)
    array_to_picture(mandelbrot_vals, cmap="magma", save_path=f"./py/fractals/pictures/mandlebrot{limit}.png")