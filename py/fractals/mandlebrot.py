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
    limit = int(input("Input the limit:\t"))
    width, height = int(input("Input width of result image:\t")), int(input("Input height of result image:\t"))

    vmandelbrot = np.vectorize(mandlebrot)
    x = np.linspace(-2.0, 1.0, width)
    y = np.linspace(-1.25, 1.25, height)
    X, Y = np.meshgrid(x, y)
    C = X + (1j * Y)

    mandelbrot_vals = vmandelbrot(C, limit=limit)
    array_to_picture(mandelbrot_vals, cmap="magma", save_path=f"./py/fractals/pictures/mandlebrot{limit}.png")
    print(f"Saved at ./py/fractals/pictures/mandlebrot{limit}.png")