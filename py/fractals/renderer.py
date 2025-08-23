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