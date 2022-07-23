from PIL import Image
import numpy as np

# 完美复刻
COLOR_MAP = dict(
    Road=(255, 255, 255),
    Building=(0, 0, 255),
    Vegetation=(0, 255, 255),
    Tree=(0, 255, 0),
    MovingCar=(255, 255, 0),
    Clutter=(255, 0, 0)
)


def render(mask_path, vis_path):
    new_mask = np.array(Image.open(mask_path)).astype(np.uint8)
    cm = np.array(list(COLOR_MAP.values())).astype(np.uint8)
    color_img = cm[new_mask]
    color_img = Image.fromarray(np.uint8(color_img))  # Image.fromarray(np.uint8(img)):array转换成image
    color_img.save(vis_path)


if __name__ == '__main__':
    mask_path = r'H:\datasets\Postdam\Mask\3780.png'
    vis_path = r'H:\datasets\Postdam\test\3780_test.png'
    render(mask_path, vis_path)
