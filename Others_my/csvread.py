import csv
import os
# 读取数据
import pandas as pd
# data = pd.read_csv("data1.csv",header=None)
data = pd.read_csv("data2.csv")  #直接将csv表中的第一行当作表头
# print(data)


# ①获取所有列，并存入一个数组中
import numpy as np
data = np.array(data)
# print(data)
# [[1366]
#  [1367]
#  [1368]
#  ...
#  [2519]
#  [2520]
#  [2521]]
from PIL import Image
import numpy as np
COLOR_MAP = dict(
        IGNORE=(0, 0, 0),
        Background=(255, 255, 255),
        Building=(255, 0, 0),
        Road=(255, 255, 0),
        Water=(0, 0, 255),
        Barren=(159, 129, 183),
        Forest=(0, 255, 0),
        Agricultural=(255, 195, 128),
    )


def render(mask_path, vis_path):
    new_mask = np.array(Image.open(mask_path)).astype(np.uint8)
    cm = np.array(list(COLOR_MAP.values())).astype(np.uint8)
    color_img = cm[new_mask]
    color_img = Image.fromarray(np.uint8(color_img))
    color_img.save(vis_path)

# 将数字数组转为字符数组
# s  =  map ( str ,data)

# str1 = ''.join(str(i) for i in data)
# print(str1)

# 遍历数组
# root = 'G:\\LoveDA\\Train\\Urban\masks_png\\'
root = 'G:\\LoveDA\\Val\\Urban\\masks_png\\'
# root_vis = 'G:\\LoveDA\\Train\\Urban\\masks_vis\\'
root_vis = 'G:\\LoveDA\\Val\\Urban\\masks_vis\\'

for element in data:
    ele_str = str(element[0])
    # str1 = ''.join(str(element))
    if __name__ == '__main__':
        # dir_root = element
        path_root = os.path.join(root, ele_str + '.png')
        vis_root = os.path.join(root_vis, ele_str + '.png')
        mask_path = path_root
        # vis_path = r'C:\Users\28123\Desktop\masks_png\13661366_vis.png'
        vis_path = vis_root
        render(mask_path, vis_path)

# numpy的array转list
# left_specturm_train.tolist()
# 用to.list()
# 既可

# list转numpy的array
# a = np.array(b)

# 字符串转list
# list_convert = a.split()  #
#
# # list转str
# str_convert = ''.join(list)


# import os,sys
# __dir__ = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(__dir__)
# sys.path.append(os.path.abspath(os.path.join(__dir__, '')))


# import csv
# with open('data1.csv', 'r') as f:
#     reader = csv.reader(f)
#     print(type(reader))
#
#     index = 1
#     for index in reader:
#         print(index)
#         index += 1



# with open('data1.csv','r',encoding="utf-8") as csvfile:  #utf-8-
#     read1 = csv.reader(csvfile)  #
#     print(type(read1))   #<class '_csv.reader'>
#     for i in read1:   #每一行都是一个列表
#         print(i)


