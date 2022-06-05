# aim：将原图裁剪成512*512，一张1024*1024的图片裁剪成4张512*512
# 或者将图片裁剪范围尽可能地裁到信息多的范围

from PIL import Image

img = Image.open('G:\LoveDA\JPEGImages\\1366.jpg')
#
# print(img.format, img.size, img.mode)


box = (100, 100, 500, 500)  # 设置要拷贝的区域

# 将im表示的图片对象拷贝到region中，大小为(400*400)像素。这个region可以用来后续的操作(region其实就是一个Image对象)，box变量是一个四元组(左，上，右，下)。
region = img.crop(box)

region = region.transpose(Image.ROTATE_180)  # 从字面上就可以看出，先把region中的Image反转180度，然后再放回到region中。
img.paste(region, box)  # 粘贴box大小的region到原先的图片对象中。