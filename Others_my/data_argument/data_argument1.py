import os
import tensorflow as tf
import torch
import random
import numpy as np
from PIL import Image, ImageOps, ImageFilter, ImageEnhance
import albumentations
from albumentations import HueSaturationValue

# 给定一张图像，随机调整图像的色彩。因为调整亮度、对比度、饱和度和色相的顺序会影
# 响最后得到的结果，所以可以定义多种不同的顺序。具体使用哪一种顺序可以在训练
# 数据预处理时随机地选择一种。这样可以进一步降低无关因素对模型的影响。

def distort_color(image, color_ordering=0):
    # 亮度：-0.125~0.125  饱和度：0.5~1.5,饱和对是对色彩的浓度（纯度）的定义  色调:0.5~1.5
    if color_ordering == 0:
        # 在(-max_delta, max_delta)的范围随机调整图像的亮度
        image = tf.image.random_brightness(image, max_delta=32. / 255.)  # 亮度
        # 在[lower, upper]的范围内随机调整图像的饱和度
        image = tf.image.random_saturation(image, lower=0.5, upper=1.5)  # 饱和度
        # 在[-max_delta, max_delta]的范围内随机调整图像的色相。max_delta的取值在[0, 0.5]之间
        image = tf.image.random_hue(image, max_delta=0.2)  # 色相
        # 在[lower, upper]的范围随机调整图的对比度
        image = tf.iamge.random_contrast(image, lower=0.5, upper=1.5)  # 对比度
    elif color_ordering == 1:
        # 在[lower, upper]的范围内随机调整图像的饱和度
        image = tf.image.random_saturation(image, lower=0.5, upper=1.5)  # 饱和度
        # 在(-max_delta, max_delta)的范围随机调整图像的亮度
        image = tf.image.random_brightness(image, max_delta=32. / 255.)  # 亮度
        # 在[lower, upper]的范围随机调整图的对比度
        image = tf.iamge.random_contrast(image, lower=0.5, upper=1.5)   # 对比度
        # 在[-max_delta, max_delta]的范围内随机调整图像的色相。max_delta的取值在[0, 0.5]之间
        image = tf.image.random_hue(image, max_delta=0.2)  # 色相
    elif color_ordering == 2:
        # 还可以定义其他的排列，但在这里就不再一一列出。
        # 在[lower, upper]的范围随机调整图的对比度
        image = tf.iamge.random_contrast(image, lower=0.5, upper=1.5)  # 对比度
        # 在[-max_delta, max_delta]的范围内随机调整图像的色相。max_delta的取值在[0, 0.5]之间
        image = tf.image.random_hue(image, max_delta=0.2)  # 色相
        # 在[lower, upper]的范围内随机调整图像的饱和度
        image = tf.image.random_saturation(image, lower=0.5, upper=1.5)  # 饱和度
        # 在(-max_delta, max_delta)的范围随机调整图像的亮度
        image = tf.image.random_brightness(image, max_delta=32. / 255.)  # 亮度

    # tf.clip_by_value():将一个张量的值限制在给定的最小值和最大值之间。对于给定的张量t，返回的张量与之有着相同的类型和相同的大小，
    # 只是它的值在clip_value_min和clip_value_max之间。任何比clip_value_min小的数设置成clip_value_min，任何比clip_value_max大的数被设置成clip_value_max.
    return tf.clip_by_value(image, 0.0, 1.0)

"""原本：
def distort_color(image, color_ordering=0):
    if color_ordering == 0:
        image = tf.image.random_brightness(image, max_delta=32. / 255.)
        image = tf.image.random_saturation(image, lower=0.5, upper=1.5)
        image = tf.image.random_hue(image, max_delta=0.2)
        image = tf.iamge.random_contrast(image, lower=0.5, upper=1.5)
    elif color_ordering == 1:
        image = tf.image.random_saturation(image, lower=0.5, upper=1.5)
        image = tf.image.random_brightness(image, max_delta=32. / 255.)
        image = tf.iamge.random_contrast(image, lower=0.5, upper=1.5)
        image = tf.image.random_hue(image, max_delta=0.2)
    elif color_ordering == 2:
        # 还可以定义其他的排列，但在这里就不再一一列出。
        ...
    return tf.clip_by_value(image, 0.0, 1.0)
"""

# 和图像翻转类似，调整图像的亮度、对比度、饱和度和色相在很多图像识别应用中都不会影响识别的结果。
# 所以在训练神经网络模型时，可以随机调整训练图像的这些属性，从而使得到的模型尽可能小地受到无关因素的影响。

class Color(object):  # 调整亮度、对比度、锐度
    def __init__(self):
        self.p = random.random()
        self.threshold = 0.3

    def __call__(self, sample):
        img = sample['image']
        mask = sample['label']

        # 当随机值达到阈值时，才对数据进行色彩调整
        if self.p > self.threshold:
            # 使用一种随机的顺序调整图像色彩。
            img = distort_color(img, np.random.randint(2))
            mask = distort_color(mask, np.random.randint(2))

        return {'image': img,
                'label': mask}

#  ******************************   实验   ********************************* #

# 调整亮度
def bright(image):
    enh_bri = ImageEnhance.Brightness(image)
    # brightness = 1.2  变亮1.5 变暗0.8 0.0产生黑色  1.0保持
    brightness = random.uniform(-0.125, 0.125)
    image_brightened = enh_bri.enhance(brightness)

    return image_brightened.convert('RGB')

# # 调整锐度
# def ruidu(image):
#     enh_sha = ImageEnhance.Sharpness(image)
#     sharpness = 2.3
#     image_sharped = enh_sha.enhance(sharpness)
#
#     return image_sharped.convert('RGB')

# 调整色度
def sedu(image):
    enh_col = ImageEnhance.Color(image)
    # color = 1.2
    color = random.uniform(0.5, 1.5)
    image_colored = enh_col.enhance(color)

    return image_colored.convert('RGB')

# 调整对比度  对比度是对画面明暗程度的定义
def duibidu(image):
    enh_con = ImageEnhance.Contrast(image)
    # contrast = 1.3
    contrast = random.uniform(0.5, 1.5)
    image_contrasted = enh_con.enhance(contrast)

    return image_contrasted.convert('RGB')

# # 将随机截取的图像调整为神经网络输入层的大小。大小调整的算法是随机选择的。
# distorted_image = tf.image.resize_image(
#     distorted_images, [height, width], method=np.random.randint(2))

# HueSaturationValue(hue_shift_limit=20,sat_shift_limit=30,val_shift_limit=20,always_apply=False,p=0.5)
# 色调饱和度值 参数：随机色调、饱和度、值变化。
# augments = HueSaturationValue(hue_shift_limit=20, sat_shift_limit=30, val_shift_limit=20,
#                                 always_apply=False, p=0.5)(image=img, mask=mask)
# # 亮度：-0.125~0.125  饱和度：0.5~1.5,饱和对是对色彩的浓度（纯度）的定义  色调:0.5~1.5
# img = bright(img)
# mask = bright(mask)
# # 对比度
# img = duibidu(img)
# mask = duibidu(mask)
# # 色度
# img = sedu(img)
# mask = sedu(mask)

#
# path_img = r'G:\test\JPEGImages'
# path_label = r'G:\test\SegmentationClass'
# path_new_img = r'G:\test\JPEGImages_'
# path_new_label = r'G:\test\SegmentationClass_'
# img_list = os.listdir(path_img)
# label_list = os.listdir(path_label)
#
# k = 0
# for i in range(len(img_list)):
#     img = Image.open(path_img + '/' + img_list[i])
#     label =Image.open(path_label + '/' + img_list[i][0:-4] + '.png')
#     # 先实例化函数
#     color_change = Color()
#     # 用函数对图像进行处理
#     img, label = color_change(img, label)

"""
# 亮度
img_bri = ImageEnhance.Brightness(img)
mask_bri = ImageEnhance.Brightness(mask)
# 锐度
img_sha = ImageEnhance.Sharpness(img)
mask_sha = ImageEnhance.Sharpness(mask)
# 色度
img_col = ImageEnhance.Color(img)
mask_col = ImageEnhance.Color(mask)
# 对比度
img_con = ImageEnhance.Contrast(img)
mask_con = ImageEnhance.Contrast(mask)
"""
