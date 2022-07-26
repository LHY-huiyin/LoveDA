import glob
import cv2

file_names = glob.glob(r'H:/datasets/Vovpotsdam/Val/RGB/*.tif')
print(file_names)
file_flags = [i.split('\\')[1].split('m')[-1].split('.')[0].split('R')[0] for i in
              file_names]  # H:/datasets/Vovpotsdam/Train/RGB\\top_potsdam_2_10_RGB.tif
num = 0

size_of_split = int(input("请输入分割的单幅图片尺寸："))

# 对验证集中的图片进行裁剪，取名为‘val_0、val_1’
for name in file_flags:
    image_rgb = cv2.imread('H:/datasets/Vovpotsdam/Val/RGB/top_potsdam' + name + 'RGB.tif')
    image_label = cv2.imread(
        'H:/datasets/Vovpotsdam/Val/Color/top_potsdam' + name + 'label.tif')  # top_potsdam_2_10_label.tif
    # print(image_rgb.shape)
    min_i = min(image_rgb.shape[0], image_label.shape[0])
    min_j = min(image_rgb.shape[1], image_label.shape[1])
    aim = 600
    gap_i = min_i // aim
    gap_j = min_j // aim
    for i in range(gap_i):  # [600, 600, 3]
        for j in range(gap_j):
            # if i == 0 or j == 0:
            #     if i == 9:  # j==0
            #         img_rgb = image_rgb[image_rgb.shape[0] - size_of_split: image_rgb.shape[0], aim * j: size_of_split + aim * j, :]
            #         img_label = image_label[image_label.shape[0] - size_of_split: image_label.shape[0], aim * j: size_of_split + aim * j, :]
            #     elif j == 9:  # i==0
            #         img_rgb = image_rgb[aim * i: size_of_split + aim * i, image_rgb.shape[1] - size_of_split: image_rgb.shape[1], :]
            #         img_label = image_label[aim * i: size_of_split + aim * i, image_label.shape[1] - size_of_split: image_label.shape[1], :]
            #     else:  # i==0 j==0 or i==0 j==1-8  or i==1-8 j==0
            #         img_rgb = image_rgb[aim * i: size_of_split + aim * i, aim * j: size_of_split + aim * j, :]
            #         img_label = image_label[aim * i: size_of_split + aim * i, aim * j: size_of_split + aim * j, :]
            if i == gap_i and j == gap_j:  # 当
                img_rgb = image_rgb[image_rgb.shape[0] - size_of_split: image_rgb.shape[0], image_rgb.shape[1] - size_of_split: image_rgb.shape[1], :]
                img_label = image_label[image_label.shape[0] - size_of_split: image_label.shape[0], image_label.shape[1] - size_of_split: image_label.shape[1], :]
            elif j == gap_j:
                img_rgb = image_rgb[aim * i: size_of_split + aim * i, image_rgb.shape[1] - size_of_split: image_rgb.shape[1], :]
                img_label = image_label[aim * i: size_of_split + aim * i, image_label.shape[1] - size_of_split: image_label.shape[1], :]
            elif i == gap_i:
                img_rgb = image_rgb[image_rgb.shape[0] - size_of_split: image_rgb.shape[0], aim * j: size_of_split + aim * j, :]
                img_label = image_label[image_label.shape[0] - size_of_split: image_label.shape[0], aim * j: size_of_split + aim * j, :]
            else:
                img_rgb = image_rgb[aim * i: size_of_split + aim * i, aim * j: size_of_split + aim * j, :]
                img_label = image_label[aim * i: size_of_split + aim * i, aim * j: size_of_split + aim * j, :]
            cv2.imwrite('H:/datasets/Vovpotsdam/Val/image/' + 'v' + str(num) + '.jpg', img_rgb)
            cv2.imwrite('H:/datasets/Vovpotsdam/Val/mask_vis/' + 'v' + str(num) + '.png', img_label)
            print(num, img_rgb.shape)
            num += 1
