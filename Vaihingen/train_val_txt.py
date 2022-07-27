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
    train_path = r'C:/Remote sensing semantic segmentation/ISPRSVaihingen/Train/image_aug'
    val_path = r'C:/Remote sensing semantic segmentation/ISPRSVaihingen/Val/image'

    dst_train = r'C:/Remote sensing semantic segmentation/ISPRSVaihingen/ImageSets/Segmentation/train.txt'
    dst_val = r'C:/Remote sensing semantic segmentation/ISPRSVaihingen/ImageSets/Segmentation/val.txt'

    to_text(train_path, dst_train)
    to_text(val_path, dst_val)