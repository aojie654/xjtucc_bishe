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
    
    # 输出文件名
    print(list_file_name_0_t, end=", ")

    # 跳过别名和字典库,以及已经转换的文件
    if ("alias.txt" in list_file_name_0_t) or ("dict.txt" in list_file_name_0_t) or ("_utf8.txt" in list_file_name_0_t):
        print("[Skiped.]")
    else:
        print("[Processing...]")
        try:
            # 以rb方式读取文件内容, 猜测编码
            open_file_source_0 = open(list_file_name_0_t, 'rb')
            read_content_0 = open_file_source_0.read()
            read_charset_0 = chardet.detect(read_content_0)['encoding']

            # 以r方式和read_charset_0编码读取文件,忽略出错字符
            open_file_source_1 = open(list_file_name_0_t, 'r', encoding=read_charset_0, errors='ignore')
            read_content_0 = open_file_source_1.read()
            open_file_source_0.close()

            # 创建一个文件名相同,后缀增加utf8的文本文件,将内容写入文件并保存
            open_file_convert_0 = open(list_file_name_0_t.replace(".txt", '') +
                                       "_utf8.txt", "w+", encoding="utf-8")
            open_file_convert_0.write(read_content_0)

        except Exception as identifier:
            print(list_file_name_0_t + " : " + str(identifier))
        finally:
            open_file_source_0.close()
            open_file_source_1.close()
            open_file_convert_0.close()
