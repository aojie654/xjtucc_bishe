from os import system as s
from subprocess import getoutput as spgop

# 输入路径
# dir0 = "/Users/aojie654/tmp/bishe_znl/textcopy"
dir0 = input("Input DIR plz(with out end of /):")

# 追加/
dir1 = dir0+'/'

# 调用find查找.txt文件
str0 = str(spgop("find "+dir0+" -name '*.txt'"))

# 定义列表l0以存放分割后的文件列表
l0 = str0.split('\n')

# 文件转码
for t in range(0, len(l0)):
    # 以GB2312读取文件内容
    # tf0 = open(l0[t], "r", encoding="utf-8")
    tf0 = open(l0[t], 'r', encoding='GB2312', errors='ignore')
    print(l0[t])
    tr0 = tf0.read()
    tf0.close()

    # 创建一个文件名相同,后缀增加utf8的文本文件

