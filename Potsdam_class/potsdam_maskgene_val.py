# 批量图片的处理
import csv
import json
import csv
import os

import cv2
import pandas as pd
from PIL import Image
import numpy as np


# 将rgb的图片读取，通过r,g,b的值来确定标签值
def mask_render(label_path, mask_path):
    img = cv2.imread(label_path)  # B G R
    new_mask = np.array(img).astype(np.uint8)

    w = new_mask.shape[0]
    h = new_mask.shape[1]
    new_mask2 = np.zeros((w, h, 3))  # 单通道  np.zeros(w, h):Cannot interpret '600' as a data type
    for i in range(0, w):
        for j in range(0, h):
            if new_mask[i, j, 0] == 255 and new_mask[i, j, 1] == 255 and new_mask[i, j, 2] == 255:
                new_mask2[i, j] = 0  # 白色：道路 (255, 255, 255)
            elif new_mask[i, j, 0] == 255 and new_mask[i, j, 1] == 0 and new_mask[i, j, 2] == 0:
                new_mask2[i, j] = 1  # 深蓝色：建筑(0, 0, 255)
            elif new_mask[i, j, 0] == 255 and new_mask[i, j, 1] == 255 and new_mask[i, j, 2] == 0:
                new_mask2[i, j, ] = 2  # 浅蓝色：植被(0, 255, 255)
            elif new_mask[i, j, 0] == 0 and new_mask[i, j, 1] == 255 and new_mask[i, j, 2] == 0:
                new_mask2[i, j] = 3  # 绿色：树(0, 255, 0)
            elif new_mask[i, j, 0] == 0 and new_mask[i, j, 1] == 255 and new_mask[i, j, 2] == 255:
                new_mask2[i, j] = 4  # 黄色：移动汽车(255, 255, 0)
            elif new_mask[i, j, 0] == 0 and new_mask[i, j, 1] == 0 and new_mask[i, j, 2] == 255:
                new_mask2[i, j] = 5  # 红色：乱堆(255, 0, 0)

    new_mask2 = np.array(new_mask2, np.uint8)
    new_mask2 = cv2.cvtColor(new_mask2, cv2.COLOR_BGR2GRAY)  # 灰度图
    cv2.imwrite(mask_path, new_mask2)  # 单通道图片


# 图片根目录
root = 'H:/datasets/Vovpotsdam/Val/mask_vis/'
save_root = 'H:/datasets/Vovpotsdam/Val/mask/'  # 存放新图片的路径

image_files = os.listdir(root)

for image in image_files:
    element = image.split('.', 1)
    label_path = os.path.join(root, element[0] + '.png')
    mask_path = os.path.join(save_root, element[0] + '.png')
    mask_render(label_path, mask_path)
