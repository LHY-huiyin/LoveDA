import tensorflow as tf
import numpy as np
import matplotlib as plt
from PIL import Image, ImageOps, ImageFilter, ImageEnhance
import random

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

# 调整亮度、对比度、锐度
class Color(object):
    def __init__(self):
        self.p = random.random()
        self.threshold = 0.3  # 阈值：30%不进行色彩增强，70%是进行的（数字需要调试）

    def __call__(self, sample):
        img = sample['image']
        mask = sample['label']

        # 当随机值达到阈值时，才对数据进行色彩调整
        if (self.p > self.threshold):
            # HueSaturationValue(hue_shift_limit=20,sat_shift_limit=30,val_shift_limit=20,always_apply=False,p=0.5)
            # 色调饱和度值 参数：随机色调、饱和度、值变化。
            # augments = HueSaturationValue(hue_shift_limit=20, sat_shift_limit=30, val_shift_limit=20,
            #                                 always_apply=False, p=0.5)(image=img, mask=mask)
            # 亮度：-0.125~0.125  饱和度：0.5~1.5,饱和对是对色彩的浓度（纯度）的定义  色调:0.5~1.5
            img = bright(img)
            mask = bright(mask)
            # 对比度
            img = duibidu(img)
            mask = duibidu(mask)
            # 色度
            img = sedu(img)
            mask = sedu(mask)

            # img.save(path_new_img + '/' + str(("%05d" % (k))) + '.jpg')
            # mask.save(path_new_label + '/' + str(("%05d" % (k))) + '.png')

        return {'image': img,
                'label': mask}
