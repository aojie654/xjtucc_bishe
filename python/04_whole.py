# -*- coding: utf-8 -*-

from os import system as s, path as p
from subprocess import getoutput as spgop
import re

# 输入路径
dir0 = input("Input DIR plz(with out end of /):")

# 调用find查找$file_pure.txt文件
find_result_0 = spgop("find "+dir0+" -name '*_03_alias.txt'")

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
        # 判断$file_04_whole.txt文件如果存在, 即已经处理过则跳过
        if p.exists(file_source_name_0.replace(
                "_03_alias.txt", "_04_whole.txt")):
            print("[Skipped.]")
            continue
        print("[Processing...]")

        # 打开#file_03_alias.txt, 读取内容并关闭文件
        open_file_alias_0 = open(file_source_name_0, 'r', encoding='utf-8')
        read_content_alias_0 = open_file_alias_0.read()
        open_file_alias_0.close()

        # 替换所有空格
        read_content_alias_0 = re.sub("\n", "", read_content_alias_0)
        
        # 保存内容至$file_04_whole.txt文件
        open_file_whole_0 = open(file_source_name_0.replace(
            "_03_alias.txt", "_04_whole.txt"), 'w+', encoding='utf-8')
        open_file_whole_0.write(read_content_alias_0)
        open_file_whole_0.close()

    except Exception as identifier:
        print(file_source_name_0+" : "+identifier)
