#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  24 10:47:36 2018

@author: yxh
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

import sys
import shutil

path = '/home/yxh/caffe/examples/fcn/IMAGES/IMAGES/'
newpath = '/home/yxh/caffe/examples/fcn/IMAGES/output/'


def turnto24(path):
    files = os.listdir(path)
    files = np.sort(files)
    i = 0
    for f in files:
        imgpath = path + f
        img = Image.open(imgpath).convert('RGB')  # 'L'转灰度图
        dirpath = newpath
        file_name, file_extend = os.path.splitext(f)
        dst = os.path.join(os.path.abspath(dirpath), file_name + '.jpg')
        img.save(dst)


turnto24(path)
