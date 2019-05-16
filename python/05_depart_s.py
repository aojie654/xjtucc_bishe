# -*- coding: utf-8 -*-

from os import system as s, path as p
from subprocess import getoutput as spgop
import re

# 输入路径
dir0 = input("Input DIR plz(with out end of /):")

# 由于不是每个作品都有别名, 因此使用find查找*_pure.txt文件
find_result_0 = str(spgop("find "+dir0+" -name '*_pure.txt'"))

# 定义列表l0以存放分割后的文件列表
list_file_name_0 = find_result_0.split('\n')

# 判断文件是否存在
for list_file_name_0_t in list_file_name_0:

    # 获取当前文件所在路径
    file_dir_0 = list_file_name_0_t[0:list_file_name_0_t.rfind('/')]

    # 获取作品名
    file_name_0 = file_dir_0[file_dir_0.rfind('/')+1:]

    try:
        # 拼接以得到文件名
        source_file_name_0 = file_dir_0+"/"+file_name_0+"_utf8_pure_single.txt"

        
        if p.exists(source_file_name_0):
            pass
        else:
            source_file_name_0 = source_file_name_0.replace("_utf8_pure_single.txt", "_utf8_pure.txt")
        print(source_file_name_0, end=", ")
        # 判断$file_single.txt文件如果存在, 即已经处理过则跳过
        if p.exists(source_file_name_0.replace(".txt", "_single.txt")):
            print("[Skiped.]")
        else:
            print("[Processing...]")
            # 打开alias.txt
            open_file_alias_0 = open(list_file_name_0_t, 'r', encoding='utf-8')

            # 读取alias.txt内容
            read_content_alias_0 = open_file_alias_0.read()
            
            # 将"["替换为"("
            read_content_alias_0 = re.sub("\[", "(", read_content_alias_0)
            
            # "]"替换为")"
            read_content_alias_0 = re.sub(",?\]", ")", read_content_alias_0)
            
            # 将','替换为')|('
            read_content_alias_0 = re.sub(",", ")|(", read_content_alias_0)

            # 将获取到的内容以换行进行分割得到内容列表
            list_alias_0 = read_content_alias_0.split('\n')

            # 打开#file_pure.txt, 读取内容
            open_file_pure_0 = open(source_file_name_0, 'r', encoding='utf-8')
            read_content_pure_0 = open_file_pure_0.read()

            # 新建词典, 以:分割,冒号的人名为key,冒号后的别名列表eval为value.
            dct_alias_0 = {}
            for list_alias_0_t0 in list_alias_0:
                """
                $1 index_of_split                                               查找':'的下标
                $2 dict_alias_0_key                                             从0下标截取到':'处,即人名
                $3 dict_alias_0_value                                           冒号后内容,即别名列表
                $4 dct_alias_0[dict_alias_0_key] = dict_alias_0_value           更新字典
                """
                index_of_split = list_alias_0_t0.find(':')
                dict_alias_0_key = list_alias_0_t0[0:index_of_split]
                dict_alias_0_value = list_alias_0_t0[index_of_split+1:]
                dct_alias_0[dict_alias_0_key] = dict_alias_0_value

            # 使用t2遍历字典的键, 使用正则表达式替换别名
            for list_alias_0_t2 in list(dct_alias_0.keys()):
                read_content_pure_0 = re.sub(
                    dct_alias_0[list_alias_0_t2], list_alias_0_t2, read_content_pure_0)

            # 保存内容至single文件
            open_file_single_0 = open(source_file_name_0.replace(
                ".txt", "_single.txt"), 'w+', encoding='utf-8')
            open_file_single_0.write(read_content_pure_0)

            # 关闭文件
            open_file_alias_0.close()
            open_file_pure_0.close()
            open_file_single_0.close()
    except Exception as identifier:
        print(list_file_name_0_t+" : "+identifier)
