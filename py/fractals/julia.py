import numpy as np
from renderer import array_to_picture

def julia(z:complex, c: complex, limit: int=5):
    for i in range(limit):
        z = z**2 + c
        if abs(z) > 2:
            return (i / limit)
    return 1

# Example usage
if __name__ == "__main__":
    limit = 100
    width, height = 1920, 1080
    x = np.linspace(-1.5, 1.5, width)
    y = np.linspace(-1.5, 1.5, height)
    X, Y = np.meshgrid(x, y)
    Z = X + (1j * Y)

    c = complex(-0.5125 , 0.5213)
    vjulia = np.vectorize(lambda z: julia(z,c, limit=limit))
    julia_vals = vjulia(Z)

    array_to_picture(julia_vals, cmap="magma", save_path=f"./py/fractals/pictures/julia{str(c)}{limit}.png")