#
# import os
# from PIL import Image
#
# dirname_read="G:/LoveDA/JPEGImages/"   #注意后面的斜杠
# dirname_write="G:/LoveDA/JPEGImages/"
# names=os.listdir(dirname_read)
# count=0
# for name in names:
#     img=Image.open(dirname_read+name)
#     name=name.split(".")
#     if name[-1] == "png":
#         name[-1] = "jpg"
#         name = str.join(".", name)
#         r,g,b,a=img.split()
#         img=Image.merge("RGB",(r,g,b))
#         to_save_path = dirname_write + name
#         img.save(to_save_path)
#         count+=1
#         print(to_save_path, "------conut：",count)
#     else:
#         continue

import os
import cv2 as cv

image_path = 'G:\\LoveDA\\Val\\Urban\\images_png\\'
save_path = 'G:\\LoveDA\\Val\\Urban\\images_jpg\\'

if not os.path.exists(save_path):
    os.makedirs(save_path)

image_file = os.listdir(image_path)

for image in image_file:
    if image.split('.')[-1] in ['bmp', 'jpg', 'jpeg', 'png', 'JPG', 'PNG']:
        str = image.rsplit(".", 1)
        output_img_name = str[0] + ".jpg"
        src = cv.imread(os.path.join(image_path, image))
        newimg = cv.imwrite(save_path + '/' + output_img_name, src)
print('FINISHED')

