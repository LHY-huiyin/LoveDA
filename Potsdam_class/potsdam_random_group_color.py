import os
import cv2 as cv

f_train = open('H:/datasets/Vovpotsdam/randomgroup/train.txt', 'r')
f_val = open('H:/datasets/Vovpotsdam/randomgroup/val.txt', 'r')

# 对彩色RGB图片进行分类，分别写入train,val中  此处是生成标注图像的
for element_rgb in f_train.readlines():
    # 读取的是数字和分行符
    element_rgb = str(element_rgb).replace("\n", "")  # top_potsdam_2_10_RGB  将换行符换成空
    # 图片的路径
    element = element_rgb.split('R')[0]
    root = os.path.join('H:\\datasets\\Postdam\\5_Labels_all\\', element + 'label.tif')
    # 图片保存的新路径
    save_path = os.path.join('H:\\datasets\\Vovpotsdam\\Train\\Color\\', element + 'label.tif')
    # 读取图片
    img = cv.imread(root)
    # 写入图片
    save_img = cv.imwrite(save_path, img)

# 对验证图片进行分类，写入val中  此处是按照给定的分组txt文件，读取其每一行的名称，再读取相应LABLE文件中的文件，并将其写入新的分组好的文件中
for element_rgb in f_val.readlines():
    # 读取的是数字和分行符
    element_rgb = str(element_rgb).replace("\n", "")  # top_potsdam_2_10_RGB  将换行符换成空
    # 图片的路径
    element = element_rgb.split('R')[0]
    root = os.path.join('H:\\datasets\\Postdam\\5_Labels_all\\', element + 'label.tif')
    # 图片保存的新路径
    save_path = os.path.join('H:\\datasets\\Vovpotsdam\\Val\\Color\\', element + 'label.tif')
    # 读取图片
    img = cv.imread(root)
    # 写入图片
    save_img = cv.imwrite(save_path, img)