import os
import cv2 as cv

f_train = open('H:/datasets/VOCPotsdam/ImageSets/Segmentation/train.txt', 'r')
f_val = open('H:/datasets/VOCPotsdam/ImageSets/Segmentation/val.txt', 'r')

# 多此一举：对于voc2017格式，只需由train.txt、val.txt文件决定其类别
# 对彩色RGB图片进行分类，分别写入train,val中  此处是生成标注图像的
for element in f_train.readlines():
    # 读取的是数字和分行符
    element = str(element).replace("\n", "")
    # element = train.split('', 0)
    # 图片的路径
    root = os.path.join('H:\\datasets\\Postdam\\Mask\\', element + '.png')
    # 图片保存的新路径
    save_path = os.path.join('H:\\datasets\\VOCPotsdam\\Train\\mask\\', element + '.png')
    # 读取图片
    img = cv.imread(root)
    # 写入图片
    save_img = cv.imwrite(save_path, img)

# 验证集
for element in f_val.readlines():
    element = str(element).replace("\n", "")
    root = os.path.join('H:\\datasets\\Postdam\\Mask\\', element + '.png')
    save_path = os.path.join('H:\\datasets\\VOCPotsdam\\Val\\mask\\', element + '.png')
    img = cv.imread(root)
    save_img = cv.imwrite(save_path, img)