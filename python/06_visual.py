# -*- coding: utf-8 -*-

from os import system as s, path as p
from subprocess import getoutput as spgop

# 输入路径
# dir0 = input("Input DIR plz(with out end of /):")
dir0 = ""

# 调用find查找$file_04_whole.txt文件
find_result_0 = spgop("find "+dir0+" -name '*_04_whole.txt'")

# 定义列表list_file_name_0以存放分割后的文件列表
list_file_name_0 = find_result_0.split('\n')

# 遍历文件列表
for list_file_name_0_t in list_file_name_0:
    # 获取当前文件所在路径
    file_dir_0 = list_file_name_0_t[0:list_file_name_0_t.rfind('/')]

    # 获取作品名
    work_name_0 = file_dir_0[file_dir_0.rfind('/')+1:]

    # 文件源即为当前遍历元素
    file_source_name_0 = list_file_name_0_t
    print(file_source_name_0+", ", end="")

    try:
        # 判断$file_05_departw.txt和$file_05_markw.txt文件如果存在, 即已经处理过则跳过
        if p.exists(file_source_name_0.replace(
                "_05_departs.txt", "_06_visuals.html")):
            print("[Skipped.]")
        else:
            print("[Processing...]")
            
