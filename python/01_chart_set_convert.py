#-*- coding：utf-8 -*-

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

    # 跳过别名和字典库,以及已经转换的文件 
    if ("alias.txt" in list_file_name_0_t) or ("dict.txt" in list_file_name_0_t) or ("_utf8.txt" in list_file_name_0_t):
        pass
    else:
        try:
            # 以rb读取文件内容, 猜测编码
            open_file_source_0 = open(list_file_name_0_t, 'rb')
            read_content_0 = open_file_source_0.read()
            read_charset_0 = chardet.detect(read_content_0)['encoding']
            
            # 将内容编码为utf-8
            read_text_0 = str(read_content_0, encoding='utf-8')
            print(list_file_name_0_t+', '+ read_charset_0)
            

            # 创建一个文件名相同,后缀增加utf8的文本文件
            open_file_convert_0 = open(list_file_name_0_t.replace(".txt", '') +
                    "_utf8.txt", "w+", encoding="utf-8")
            open_file_convert_0.write(read_text_0)

        except Exception as identifier:
            print(identifier)
        finally:
            open_file_source_0.close()
            open_file_convert_0.close()
