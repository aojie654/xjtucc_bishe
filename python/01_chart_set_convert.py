# -*- coding: utf-8 -*-

from os import system as s
from subprocess import getoutput as spgop
import chardet

# 输入路径
dir0 = input("Input DIR plz(with out end of /):")

# 追加/
dir1 = dir0+'/'

# 调用find查找.txt文件
find_result_0 = str(spgop("find "+dir0+" -name '*.txt'"))

# 定义列表l0以存放分割后的文件列表
list_file_name_0 = find_result_0.split('\n')

# 文件转码
for list_file_name_0_t in list_file_name_0:
    
    # 文件源即为当前遍历元素
    file_source_name_0 = list_file_name_0_t
    print(file_source_name_0+", ", end="")

    # 跳过别名和字典库,以及已经转换的文件
    if ("alias.txt" in file_source_name_0) or ("dict.txt" in file_source_name_0) or ("_utf8.txt" in file_source_name_0):
        print("[Skipped.]")
    else:
        print("[Processing...]")
        try:
            # 以rb方式读取文件内容, 猜测编码
            open_file_source_rb_0 = open(file_source_name_0, 'rb')
            read_content_0 = open_file_source_rb_0.read()
            open_file_source_rb_0.close()
            read_charset_0 = chardet.detect(read_content_0)['encoding']

            # 以r方式和read_charset_0编码读取文件,忽略出错字符
            open_file_source_0 = open(file_source_name_0, 'r', encoding=read_charset_0, errors='ignore')
            read_content_0 = open_file_source_0.read()
            open_file_source_0.close()

            # 创建一个文件名相同,后缀增加utf8的文本文件,将内容写入文件并保存
            open_file_utf8_0 = open(file_source_name_0.replace(".txt", '') +
                                       "_utf8.txt", "w+", encoding="utf-8")
            open_file_utf8_0.write(read_content_0)
            open_file_utf8_0.close()

        except Exception as identifier:
            print(file_source_name_0 + " : " + str(identifier))
