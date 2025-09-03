import numpy as np
from renderer import array_to_picture

def julia(z:complex, c: complex, limit: int=5):
    for i in range(limit):
        z = z**2 + c
        if abs(z) > 2:
            return (i / limit)
    return 0

# Example usage
if __name__ == "__main__":
    limit = int(input("Input the limit:\t"))
    width, height = int(input("Input width of result image:\t")), int(input("Input height of result image:\t"))
    C = complex(input("Input complex (1+1j format):\t"))
    
    x = np.linspace(-1.5, 1.5, width)
    y = np.linspace(-1.5, 1.5, height)
    X, Y = np.meshgrid(x, y)
    Z = X + (1j * Y)

    vjulia = np.vectorize(lambda z: julia(z,C, limit=limit))
    julia_vals = vjulia(Z)

    array_to_picture(julia_vals, cmap="magma", save_path=f"./py/fractals/pictures/julia{str(C)}{limit}.png")
    print(f"Saved at ./py/fractals/pictures/julia{str(C)}{limit}.png")