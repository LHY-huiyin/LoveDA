import matplotlib.pyplot as plt
import numpy as np
import torch
import cv2

def get_pascal_labels():
    return np.array([[0, 1],
                     [0, 1],
                     [0, 1],  # 红：建筑
                     [0, 1],  # 黄：马路
                     [0, 1],  # 蓝：水
                     [0, 1],  # 紫色：荒地
                     [0, 1],  # 绿：森林
                     [0, 1]])  # 橙：农田   RGB格式

img_path = r'G:\\LoveDA\\SegmentationClass\\1366.png'
n_classes = 8
label_mask = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

w, h = label_mask.shape[0], label_mask.shape[1]
# 将每个通道的图片都进行处理：为甚batch_size = 5,通道数便是5
# 原本是灰色图（r=g=b），现在将r,g,b的颜色分别涂上标签的像素值————先copy然后对应位置上色
c0 = label_mask.copy()  # (512, 512)
c1 = label_mask.copy()
c2 = label_mask.copy()
c3 = label_mask.copy()
c4 = label_mask.copy()
c5 = label_mask.copy()
c6 = label_mask.copy()
c7 = label_mask.copy()

label_colours = get_pascal_labels()

for ll in range(0, n_classes):  # RGB对应位置上色
    # 将灰度图中标签为0/1/2/3/4/5/6/7的值换成想对应的标签0/1/2/3/4/5/6/7所对应的像素值
    # 将标签为0的通道中，为0则赋值为1，其他为0（转为两种颜色）  因为输出结果的值为0，1
    # for i in range(w):
    #     for j in range(h):
    #         if c0[i][j] == ll:
    #             c0[i][j] = 1
    #         else:
    #             c0[i][j] = 0
    if ll == 0:
        c0[label_mask == ll] = label_colours[ll, 1]
        c0[label_mask != ll] = label_colours[ll, 0]
    if ll == 1:
        c1[label_mask == ll] = label_colours[ll, 1]
        c1[label_mask != ll] = label_colours[ll, 0]
    if ll == 2:
        c2[label_mask == ll] = label_colours[ll, 1]
        c2[label_mask != ll] = label_colours[ll, 0]
    if ll == 3:
        c3[label_mask == ll] = label_colours[ll, 1]
        c3[label_mask != ll] = label_colours[ll, 0]
    if ll == 4:
        c4[label_mask == ll] = label_colours[ll, 1]
        c4[label_mask != ll] = label_colours[ll, 0]
    if ll == 5:
        c5[label_mask == ll] = label_colours[ll, 1]
        c5[label_mask != ll] = label_colours[ll, 0]
    if ll == 6:
        c6[label_mask == ll] = label_colours[ll, 0]
        c6[label_mask != ll] = label_colours[ll, 0]
    if ll == 7:
        c7[label_mask == ll] = label_colours[ll, 0]
        c7[label_mask != ll] = label_colours[ll, 0]

    # 0号标签：[255, 255, 255]白色--> [0,0]=255  [0,1]=255  [0,2]=255
# 定义一个为0的三通道数组,组合为BGR
mask = np.zeros((label_mask.shape[0], label_mask.shape[1], 8))  # （513，513，3）
mask[:, :, 0] = c0   # rgb[:, :, 0]代表的第一个通道 could not broadcast input array from shape (513,513,3) into shape (513,513)
mask[:, :, 1] = c1
mask[:, :, 2] = c2
mask[:, :, 3] = c3
mask[:, :, 4] = c4
mask[:, :, 5] = c5
mask[:, :, 6] = c6
mask[:, :, 7] = c7

# rgb = np.zeros((3, label_mask.shape[0], label_mask.shape[1]))  # （3, 513，513）
# rgb[0, :, :] = r / 255.0  # rgb[:, :, 0]代表的第一个通道 could not broadcast input array from shape (513,513,3) into shape (513,513)
# rgb[1, :, :] = g / 255.0
# rgb[2, :, :] = b / 255.0
# rgb的值是0,1 黑白图片：只有当像素值为255的时候才为1

