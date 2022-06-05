# encoding: utf-8
import os


def to_text(src, dst1):
    txt = []
    filenames = os.listdir(src)
    for item in filenames:
        # if item.endswith('.png'):
        name = item.split('.')[0]
        txt.append(name)

    fo = open(dst1, 'w')
    for m in txt:
        fo.write(str(m) + '\n')


if __name__ == "__main__":
    src_train = r'G:\\test\\Train\\images_png'
    dst_train = r'G:\\test\\Train\\train.txt'
    to_text(src_train, dst_train)

    src_val = r'G:\\test\\Val\\images_png'
    dst_val = r'G:\\test\\Val\\val.txt'
    to_text(src_val, dst_val)

    src_val = r'G:\\test\\Test\\images_png'
    dst_val = r'G:\\test\\Test\\test.txt'
    to_text(src_val, dst_val)


"""初始：
if __name__ == "__main__":
    # src = r'G:\\LoveDA\\Test\\Urban\\images_png'
    src = r'G:\\LoveDA\\Train\\Urban\\test'
    # dst1 = r'G:\\LoveDA\\Test\\Urban\\test.txt'
    dst1 = r'G:\\LoveDA\\Train\\Urban\\test\\test.txt'
    to_text(src, dst1)
"""
