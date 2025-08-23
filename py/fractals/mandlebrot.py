import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def array_to_picture(arr, cmap="viridis", save_path=None):
    height, width = arr.shape
    dpi = 100
    fig = plt.figure(figsize=(width / dpi, height / dpi), dpi=dpi)
    plt.imshow(arr, cmap=cmap, extent=(0, width, 0, height))
    plt.axis("off")

    if save_path:
        plt.savefig(save_path, bbox_inches="tight", pad_inches=0)
    plt.show()
    plt.close(fig)
    return

def mandlebrot(c: complex, limit: int=5):
    z = 0 + 0j
    for i in range(limit):
        z = z**2 + c
        if abs(z) > 2:
            return (i / limit)
    return 1

# Example usage
if __name__ == "__main__":
    vmandelbrot = np.vectorize(mandlebrot)
    width, height = 3840, 2160
    x = np.linspace(-2.0, 1.0, width)
    y = np.linspace(-1.25, 1.25, height)
    X, Y = np.meshgrid(x, y)
    C = X + (1j * Y)

    mandelbrot_vals = vmandelbrot(C, limit=100)
    array_to_picture(mandelbrot_vals, cmap="magma", save_path="./py/fractals/mandlebrot.png")