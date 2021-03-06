# -*- coding: utf-8 -*-

from os import system as s
from subprocess import getoutput as spgop
import glob as gb

# 输入需要根据txt文件名创建文件夹的路径
dir0 = input("Input DIR plz(with out end of /):")

# 查找.txt文件
find_result_0 = spgop("find "+dir0+" -name '*.txt'")

# 将文件列表以回车切存至列表
list_file_name_0 = find_result_0.split('\n')
list_file_create_0 = []

# 根据文件名去掉.txt创建列表，并忽略已经创建的文件夹
for list_file_name_0_t in list_file_name_0:
    list_file_name_0_t = list_file_name_0_t.replace(dir0+"/", '')
    list_file_name_0_t = list_file_name_0_t.replace(".txt", '')
    print(list_file_name_0_t+", ", end="")

    if '/' in list_file_name_0_t:
        print("[Skipped.]")
        continue
    print("[Processing...]")
    list_file_create_0.append(list_file_name_0_t)

# 调用mkdir创建文件夹并将文件移动至各自的文件夹内
for list_file_create_0_t in list_file_create_0:
    s("mkdir "+dir0+"/"+list_file_create_0_t)
    s("mv "+dir0+"/"+list_file_create_0_t+".txt "+dir0+"/"+list_file_create_0_t)
