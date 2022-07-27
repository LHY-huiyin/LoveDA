# encoding: utf-8
import os


def to_text(src, dst1):
    txt = []
    filenames = os.listdir(src)
    for item in filenames:
        name = item.split('.')[0]
        txt.append(name)

    fo = open(dst1, 'w')
    for m in txt:
        fo.write(str(m) + '\n')


if __name__ == "__main__":
    train_path = r'H:\\datasets\\Vovpotsdam\\Train\\image_aug'
    val_path = r'H:\\datasets\\Vovpotsdam\\Val\\image'

    dst_train = r'H:\\datasets\\Vovpotsdam\\ImageSets\\Segmentation\\train.txt'
    dst_val = r'H:\\datasets\\Vovpotsdam\\ImageSets\\Segmentation\\val.txt'

    to_text(train_path, dst_train)
    to_text(val_path, dst_val)