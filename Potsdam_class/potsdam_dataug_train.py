"""
本代码共采用了四种数据增强，如采用其他数据增强方式，可以参考本代码，随意替换。
imageDir 为原数据集的存放位置
saveDir  为数据增强后数据的存放位置
"""
from PIL import Image
from PIL import ImageEnhance
import os
import cv2
import numpy as np
import random
from torchvision import transforms as transforms
import torchvision.transforms.functional as TF

def flip(image, label):  # 翻转图像
    # img = Image.open(os.path.join(root_path, img_name))
    image_flip = image.transpose(Image.FLIP_LEFT_RIGHT)
    label_flip = label.transpose(Image.FLIP_LEFT_RIGHT)
    # filp_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    # filp_img.save(os.path.join(root_path,img_name.split('.')[0] + '_flip.jpg'))
    return image_flip, label_flip

"""
def rotation(root_path, img_name):
    # img = Image.open(os.path.join(root_path, img_name))
    values = [20, 90, 180, 270]
    angle = random.choice(values)
    rotation_img = img.rotate(angle)  # 旋转角度
    # rotation_img.save(os.path.join(root_path,img_name.split('.')[0] + '_rotation.jpg'))
    return rotation_img
"""
def rotation(image, label):
    # img = Image.open(os.path.join(root_path, img_name))
    values = [20, 90, 180, 270]
    angle = random.choice(values)
    image_rotated = image.rotate(angle)
    label_rotated = label.rotate(angle)
    # rotation_img = img.rotate(angle)  # 旋转角度
    # rotation_img.save(os.path.join(root_path,img_name.split('.')[0] + '_rotation.jpg'))
    return image_rotated, label_rotated

# 色度、亮度、饱和度、对比度的变化  随机改变图像
def BCSH_transform(image):
    # image = Image.open(os.path.join(root_path, img_name))
    im = transforms.ColorJitter(brightness=0.6)(image)  # [max(0, 1 - brightness), 1 + brightness]
    im = transforms.ColorJitter(contrast=0.3)(im)  # [max(0, 1 - contrast), 1 + contrast]
    im = transforms.ColorJitter(saturation=0.6)(im)  # [max(0, 1 - saturation), 1 + saturation]
    im = transforms.ColorJitter(hue=0.08)(im)  # [-hue, hue]
    return im

# 原图和标签
image_root = "H:\\datasets\\Vovpotsdam\\Train\\image\\"  # 要改变的图片的路径文件夹
image_save = "H:\\datasets\\Vovpotsdam\\Train\\image_aug\\"  # 要保存的图片的路径文件夹
label_root = "H:\\datasets\\Vovpotsdam\\Train\\mask\\"
label_save = "H:\\datasets\\Vovpotsdam\\Train\\mask_aug\\"


for names in os.listdir(image_root):
    name = names.split('.')[0]
    name_img = name + '.jpg'
    name_label = name + '.png'
    # 原图和标签的图片名字一致，标签的图片不需要改变
    # saveName = "id" +name[:-4] + ".jpg"
    saveName_img = "id" + name + ".jpg"
    saveName_label = "id" + name + ".png"
    img = Image.open(os.path.join(image_root, name_img))
    label = Image.open(os.path.join(label_root, name_label))
    img.save(os.path.join(image_save, saveName_img))
    label.save(os.path.join(label_save, saveName_label))

    # 名字一致，标签的图片不需要改变
    # saveName = "bcsh" + name[:-4] + ".jpg"
    saveName_img = "bcsh" + name + ".jpg"
    saveName_label = "bcsh" + name + ".png"
    img_bcsh = BCSH_transform(img)
    # label_bcsh = Image.open(os.path.join(label_root, name))
    img_bcsh.save(os.path.join(image_save, saveName_img))
    label.save(os.path.join(label_save, saveName_label))

    # 名字一致，标签的图片需要随原图变化
    # saveName = "fl" + name[:-4] + ".jpg"
    saveName_img = "fl" + name + ".jpg"
    saveName_label = "fl" + name + ".png"
    # img_fl = Image.open(os.path.join(image_root, name))
    # label_fl = Image.open(os.path.join(label_root, name))
    img_fl, label_fl = flip(img, label)
    img_fl.save(os.path.join(image_save, saveName_img))
    label_fl.save(os.path.join(label_save, saveName_label))

    # 名字一致，标签的图片需要随原图变化
    # saveName = "ro" + name[:-4] + ".jpg"
    saveName_img = "ro" + name + ".jpg"
    saveName_label = "ro" + name + ".png"
    # img_ro = Image.open(os.path.join(image_root, name))
    # label_ro = Image.open(os.path.join(label_root, name))
    img_ro, label_ro = rotation(img, label)
    img_ro.save(os.path.join(image_save, saveName_img))
    label_ro.save(os.path.join(label_save, saveName_label))

