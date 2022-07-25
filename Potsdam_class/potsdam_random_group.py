import os
import random

random.seed(10)  # 设置随机数种子,复现随机场景所必须的  为了获得相同的随机数

tifFilePath = r'H:\\datasets\\Postdam\\2_Ortho_RGB\\'
saveBasePath = r"H:\\datasets\\Vovpotsdam\\randomgroup\\"

trainval_percent = 1  # trainval_percent=0.9# 表示余下的百分之十用于test
train_percent = 0.7  # train_percent=1 # 表示训练集中用于训练，没有用于验证

temp_tif = os.listdir(tifFilePath)  # 获得一个列表,每个元素是一个文件名
total_tif = []  # 用于保存所有jpg文件的文件名
for jpg in temp_tif:  # 遍历文件夹下所有文件
    if jpg.endswith(".tif"):  # 判断文件名是否以.tif结尾
        total_tif.append(jpg)

num = len(total_tif)  # 所有tif文件的总数
indices = list(range(num))  # 获得迭代类型,0 ~ (num-1)
tv = int(num * trainval_percent)  # 用于训练和验证的数量
tr = int(tv * train_percent)  # 用于训练的数量
trainval = random.sample(indices, tv)  # 用于训练和验证的样本的索引
train = random.sample(trainval, tr)  # 用于训练的样本的索引

print("train and validation set size:", tv)  # 训练样本和验证样本的总数
print("train set size:", tr)  # 训练样本的数量
ftrainval = open(os.path.join(saveBasePath, 'trainval.txt'), 'w')  # 依次打开4个文件
# ftest = open(os.path.join(saveBasePath, 'test.txt'), 'w')
ftrain = open(os.path.join(saveBasePath, 'train.txt'), 'w')
fval = open(os.path.join(saveBasePath, 'val.txt'), 'w')

for i in indices:
    name = total_tif[i][:-4] + '\n'  # 文件名+'\n',其中文件名不含.tif
    if i in trainval:  # 训练集和验证集的索引
        ftrainval.write(name)  # 写入训练和验证的文件中
        if i in train:  # 训练集的索引
            ftrain.write(name)  # 写入训练的文件中
        else:
            fval.write(name)  # 写入验证的文件中
    # else:
    #     ftest.write(name)  # 否则归于测试集,写入测试的文件中

ftrainval.close()  # 依次关闭4个文件
ftrain.close()
fval.close()
# ftest.close()

