from os import system as s
from subprocess import getoutput as spgop

# 输入需要根据txt文件名创建文件夹的路径
dir0 = input("Input DIR plz(with out end of /):")

# 追加/
dir1 = dir0+'/'

# 查找.txt文件
str0 = str(spgop("find "+dir0+" -name '*.txt'"))

# 将文件列表以回车切存至列表
l0 = str0.split('\n')
l1 = []

# 根据文件名去掉.txt创建列表，并忽略已经创建的文件夹
for t in range(len(l0)):
    l0[t-1] = l0[t-1].replace(dir1, '')
    l0[t-1] = l0[t-1].replace(".txt", '')
    if '/' not in l0[t-1]:
        l1.append(l0[t-1])
    else:
        continue

# 调用mkdir创建文件夹并将文件移动至各自的文件夹内
for t in l1:
    s("mkdir "+dir1+t)
    s("mv "+dir1+t+".txt "+dir1+t)
