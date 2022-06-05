import cv2
import numpy
import os
import pandas as pd

"""
# 测试集
img1_root = 'G:\\LoveDA\\Test\\Urban\\images_png\\'  # 读取RGB原图像
img1_sav = 'G:\\loveda_a\\Test\\images_png\\'  # 存放路径
"""

# """
# 验证集
img1_root = 'G:\\LoveDA\\Val\\Urban\\images_png\\'  # 读取RGB原图像
img1_sav = 'G:\\loveda_a\\Val\\images_png\\'  # 存放路径

img2_root = 'G:\\LoveDA\\Val\\Urban\\masks_png\\'  # 读取Labels图像
img2_sav = 'G:\\loveda_a\\Val\\masks_png\\'

img3_root = 'G:\\LoveDA\\Val\\Urban\\masks_vis\\'  # 读取Labels_color图像
img3_sav = 'G:\\loveda_a\\Val\\masks_vis\\'
# """

"""
# 训练集
img1_root = 'G:\\LoveDA\\Train\\Urban\\images_png\\'  # 读取RGB原图像
img1_sav = 'G:\\loveda_a\\Train\\images_png\\'  # 存放路径

img2_root = 'G:\\LoveDA\\Train\\Urban\\masks_png\\'  # 读取Labels图像   由于标签文件是单通道的，所以保存方式需要调整！！！
img2_sav = 'G:\\loveda_a\\Train\\masks_png\\'

img3_root = 'G:\\LoveDA\\Train\\Urban\\masks_vis\\'  # 读取Labels_color图像
img3_sav = 'G:\\loveda_a\\Train\\masks_vis\\'
"""

"""
#初始:
img1_root = 'G:\\LoveDA\\JPEGImages\\'  # 读取RGB原图像
img1_sav = 'G:\\loveda_a\\JPEGImages\\'  # 存放路径

img2_root = 'G:\\LoveDA\\SegmentationClass\\'  # 读取Labels图像  出错！！
img2_sav = 'G:\\loveda_a\\SegmentationClass\\'

img3_root = 'G:\\LoveDA\\SegmentationColor\\'  # 读取Labels_color图像
img3_sav = 'G:\\loveda_a\\SegmentationColor\\'
"""

# 读取数据
# data = pd.read_csv("data1.csv",header=None)
# data = pd.read_csv("data2.csv")  #直接将csv表中的第一行当作表头
# dirs1 = os.listdir(img1_root)
dirs2 = os.listdir(img2_root)
# dirs3 = os.listdir(img3_root)

# for element in dirs1:  # 原图像保存为jpg
#     root = os.path.join(img1_root, element)
#     img1 = cv2.imread(root)  # [1024,1024,3]
#     # 因为1024/256= 4，所以1024*1024的图像可以划分为4*4个256x256大小的图像
#     for i in range(2):
#         for j in range(2):
#             img1_ = img1[512 * i: 512 * (i + 1), 512 * j: 512 * (j + 1), :]
#
#             name_ = i * 2 + j
#             # 让RGB图像和标签图像的文件名对应
#             name_ = str(name_)
#             if element.split('.')[-1] in ['bmp', 'jpg', 'jpeg', 'png', 'JPG', 'PNG']:
#                 ele = element.rsplit(".", 1)
#                 name = ele[0] + '_' + name_
#
#             cv2.imwrite(img1_sav + name + '.jpg', img1_)  # 所有的RGB图像都放到jpg文件夹下

for element in dirs2:
    root = os.path.join(img2_root, element)
    img2 = cv2.imread(root)  # [1024,1024,3]
    # 因为1024/256= 4，所以1024*1024的图像可以划分为4*4个256x256大小的图像
    for i in range(2):
        for j in range(2):
            img2_ = img2[512 * i: 512 * (i + 1), 512 * j: 512 * (j + 1)]

            name_ = i * 2 + j
            # 让RGB图像和标签图像的文件名对应
            name_ = str(name_)
            if element.split('.')[-1] in ['bmp', 'jpg', 'jpeg', 'png', 'JPG', 'PNG']:
                ele = element.rsplit(".", 1)
                name = ele[0] + '_' + name_

            cv2.imwrite(img2_sav + name + '.png', img2_)  # 所有的标签图像都放到png文件夹下


# for element in dirs3:
#     root = os.path.join(img3_root, element)
#     img3 = cv2.imread(root)  # [1024,1024,3]
#     # 因为1024/256= 4，所以1024*1024的图像可以划分为4*4个256x256大小的图像
#     for i in range(2):
#         for j in range(2):
#             img3_ = img3[512 * i: 512 * (i + 1), 512 * j: 512 * (j + 1), :]
#
#             name_ = i * 2 + j
#             # 让RGB图像和标签图像的文件名对应
#             name_ = str(name_)
#             if element.split('.')[-1] in ['bmp', 'jpg', 'jpeg', 'png', 'JPG', 'PNG']:
#                 ele = element.rsplit(".", 1)
#                 name = ele[0] + '_' + name_
#
#             cv2.imwrite(img3_sav + name + '.png', img3_)

"""初始
img1 = cv2.imread('/Users/fuhao7i/Desktop/北漠/ISPRS遥感图像分割/2_Ortho_RGB/top_potsdam_2_10_RGB.tif')  # 读取RGB原图像

img2 = cv2.imread('/Users/fuhao7i/Desktop/北漠/ISPRS遥感图像分割/5_Labels_all/top_potsdam_2_10_label.tif')  # 读取Labels图像

# 因为6000/224 = 26，所以6000x6000的图像可以划分为26x26个224x224大小的图像
for i in range(26):
    for j in range(26):
        img1_ = img1[224 * i: 224 * (i + 1), 224 * j: 224 * (j + 1), :]
        img2_ = img2[224 * i: 224 * (i + 1), 224 * j: 224 * (j + 1), :]

        name = i * 26 + j
        # 让RGB图像和标签图像的文件名对应
        name = str(name)
        cv2.imwrite('./jpg/' + name + '.jpg', img1_)  # 所有的RGB图像都放到jpg文件夹下
        cv2.imwrite('./png/' + name + '.png', img2_)  # 所有的标签图像都放到png文件夹下
"""


