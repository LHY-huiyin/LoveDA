import glob
import cv2

file_names = glob.glob(r'H:/datasets/Vovpotsdam/Val/RGB/*.tif')
print(file_names)
file_flags = [i.split('\\')[1].split('m')[-1].split('.')[0].split('R')[0] for i in file_names]  # H:/datasets/Vovpotsdam/Train/RGB\\top_potsdam_2_10_RGB.tif
num = 0

size_of_split = int(input("请输入分割的单幅图片尺寸："))


# 对验证集中的图片进行裁剪，取名为‘val_0、val_1’
for name in file_flags:
    image_rgb = cv2.imread('H:/datasets/Vovpotsdam/Val/RGB/top_potsdam' + name + 'RGB.tif')
    image_label = cv2.imread('H:/datasets/Vovpotsdam/Val/Color/top_potsdam' + name + 'label.tif')  # top_potsdam_2_10_label.tif
    # print(image_rgb.shape)
    min_i = min(image_rgb.shape[0], image_label.shape[0])
    min_j = min(image_rgb.shape[1], image_label.shape[1])
    for i in range(min_i // size_of_split):  # [512, 512, 3]
        for j in range(min_j // size_of_split):
            img_rgb = image_rgb[size_of_split * i: size_of_split * (i + 1), size_of_split * j: size_of_split * (j + 1), :]
            img_label = image_label[size_of_split * i: size_of_split * (i + 1), size_of_split * j: size_of_split * (j + 1), :]

            cv2.imwrite('H:/datasets/Vovpotsdam/Val/image/' + 'val_' + str(num) + '.jpg', img_rgb)
            cv2.imwrite('H:/datasets/Vovpotsdam/Val/mask_vis/' + 'val_' + str(num) + '.png', img_label)
            print(num, img_rgb.shape)
            num += 1