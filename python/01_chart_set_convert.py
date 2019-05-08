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
for t in l0:

    # 跳过别名和字典库,以及已经转换的文件 
    if ("alias.txt" in t) or ("dict.txt" in t) or ("_utf8.txt" in t):
        pass
    else:
        try:
            # 以GB2312读取文件内容, 忽略无法转码部分
            tf0 = open(t, 'r', encoding='GB2312', errors='ignore')
            print(t)
            tr0 = tf0.read()
            tf0.close()

            # 创建一个文件名相同,后缀增加utf8的文本文件
            tf0 = open(t.replace(".txt", '') +
                       "_utf8.txt", "w+", encoding="utf-8")
            tf0.write(tr0)
        except Exception as identifier:
            print(identifier)
        finally:
            tf0.close()
