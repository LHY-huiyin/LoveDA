# 将三通道转为单通道 8位
# img1 = cv2.imread("G:\LoveDA\SegmentationClass\\1366.png")
# shape = img1.shape
# print(shape)

import os
import cv2

def get_path(path):
    #  返回目录中所有PNG图像的文件名列表
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.png')]

# all
pth = get_path('G:\\loveda_a\\SegmentationClass\\')
# 训练集
pth_train = get_path('G:\\loveda_a\\Train\\masks_png\\')
# 验证集
pth_val = get_path('G:\\loveda_a\\Val\\masks_png\\')

for img in pth:
    src = cv2.imread(img)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 彩图转为灰度图
    cv2.imwrite('G:\\loveda_a\\SegmentationClass\\' + img.split('\\')[-1], gray)  # 将图像写出到磁盘中
for img in pth_train:
    src = cv2.imread(img)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 彩图转为灰度图
    cv2.imwrite('G:\\loveda_a\\Train\\masks_png\\' + img.split('\\')[-1], gray)  # 将图像写出到磁盘中
for img in pth:
    src = cv2.imread(img)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 彩图转为灰度图
    cv2.imwrite('G:\\loveda_a\\Val\\masks_png\\' + img.split('\\')[-1], gray)  # 将图像写出到磁盘中
print('灰度图 Save OK!')
