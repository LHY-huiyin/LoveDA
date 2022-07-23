import glob
import cv2

file_names = glob.glob(r'H:/datasets/Postdam/2_Ortho_RGB/*.tif')
print(file_names)
file_flags = [i.split('\\')[1].split('m')[-1].split('.')[0].split('R')[0] for i in file_names]  # H:/datasets/Postdam/2_Ortho_RGB\\top_potsdam_2_10_RGB.tif
num = 0

size_of_split = int(input("请输入分割的单幅图片尺寸："))

for name in file_flags:
    image_rgb = cv2.imread('H:/datasets/Postdam/2_Ortho_RGB/top_potsdam' + name + 'RGB.tif')
    image_label = cv2.imread('H:/datasets/Postdam/5_Labels_all/top_potsdam' + name + 'label.tif')  # top_potsdam_2_10_label.tif
    # print(image_rgb.shape)
    min_i = min(image_rgb.shape[0], image_label.shape[0])
    min_j = min(image_rgb.shape[1], image_label.shape[1])
    for i in range(min_i // size_of_split):  # [512, 512, 3]
        for j in range(min_j // size_of_split):
            img_rgb = image_rgb[size_of_split * i: size_of_split * (i + 1), size_of_split * j: size_of_split * (j + 1), :]
            img_label = image_label[size_of_split * i: size_of_split * (i + 1), size_of_split * j: size_of_split * (j + 1), :]

            cv2.imwrite('H:/datasets/Postdam/RGB/' + str(num) + '.jpg', img_rgb)
            cv2.imwrite('H:/datasets/Postdam/Label/' + str(num) + '.png', img_label)
            print(num, img_rgb.shape)
            num += 1

# img1 = cv2.imread('H:/datasets/Postdam/2_Ortho_RGB/top_potsdam_2_10_RGB.tif')  # 读取RGB原图像
#
# img2 = cv2.imread('/Users/fuhao7i/Desktop/北漠/ISPRS遥感图像分割/5_Labels_all/top_potsdam_2_10_label.tif')  # 读取Labels图像
#
# # 因为6000/224 = 26，所以6000x6000的图像可以划分为26x26个224x224大小的图像
# for i in range(26):
#     for j in range(26):
#         img1_ = img1[224 * i: 224 * (i + 1), 224 * j: 224 * (j + 1), :]
#         img2_ = img2[224 * i: 224 * (i + 1), 224 * j: 224 * (j + 1), :]
#
#         name = i * 26 + j
#         # 让RGB图像和标签图像的文件名对应
#         name = str(name)
#         cv2.imwrite('./jpg/' + name + '.jpg', img1_)  # 所有的RGB图像都放到jpg文件夹下
#         cv2.imwrite('./png/' + name + '.png', img2_)  # 所有的标签图像都放到png文件夹下