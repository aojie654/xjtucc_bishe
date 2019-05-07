from os import system as s
from subprocess import getoutput as spgop

# 输入需要根据txt文件名创建文件夹的路径
dir0 = input("Input DIR plz(with out end of /):")

# 查找.txt文件
str0 = str(spgop("find "+dir0+" -name '*.txt'"))

# 将文件列表以回车切存至列表
l0 = str0.split('\n')
l1 = []

# 根据文件名去掉.txt创建列表，并忽略已经创建的文件夹
for t in l0:
    t = t.replace(dir0+"/", '')
    t = t.replace(".txt", '')
    if '/' in t:
        pass
    else:
        l1.append(t)

# 调用mkdir创建文件夹并将文件移动至各自的文件夹内
for t in l1:
    s("mkdir "+dir0+"/"+t)
    s("mv "+dir0+"/"+t+".txt "+dir0+"/"+t)
