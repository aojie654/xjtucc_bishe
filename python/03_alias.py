# -*- coding: utf-8 -*-

from os import system as s, path as p
from subprocess import getoutput as spgop
import re

# 输入路径
dir0 = input("Input DIR plz(with out end of /):")

# 调用find查找$file_pure.txt文件
find_result_0 = spgop("find "+dir0+" -name '*_02_pure.txt'")

# 定义列表list_file_name_0以存放分割后的文件列表
list_file_name_0 = find_result_0.split('\n')

# 遍历文件列表
for list_file_name_0_t in list_file_name_0:

    # 获取当前文件所在路径
    file_dir_0 = list_file_name_0_t[0:list_file_name_0_t.rfind('/')]

    # 获取作品名
    work_name_0 = file_dir_0[file_dir_0.rfind('/')+1:]

    # 拼接以得到alias绝对路径
    file_alias_name_0 = file_dir_0+"/alias.txt"

    # 文件源即为当前遍历元素
    file_source_name_0 = list_file_name_0_t
    print(file_source_name_0+", ", end="")

    try:
        # 判断$file_03_alias.txt文件如果存在, 即已经处理过则跳过
        if p.exists(file_source_name_0.replace(
                "_02_pure.txt", "_03_alias.txt")):
            print("[Skipped.]")
            continue
        print("[Processing...]")

        # 打开#file_02_pure.txt, 读取内容并关闭文件
        open_file_pure_0 = open(file_source_name_0, 'r', encoding='utf-8')
        read_content_pure_0 = open_file_pure_0.read()
        open_file_pure_0.close()

        # 若存在alias, 则进行别名替换
        if p.exists(file_alias_name_0):

            # open_file_alias_0打开alias.txt
            open_file_alias_0 = open(
                file_alias_name_0, 'r', encoding='utf-8')

            # 读取alias.txt内容并关闭文件
            read_content_alias_0 = open_file_alias_0.read()
            open_file_alias_0.close()

            # 将"["替换为"("
            read_content_alias_0 = re.sub("\[", "(", read_content_alias_0)

            # "]"替换为")"
            read_content_alias_0 = re.sub(
                ",?\]", ")", read_content_alias_0)

            # 将','替换为')|('
            read_content_alias_0 = re.sub(",", ")|(", read_content_alias_0)

            # 将获取到的内容以换行进行分割得到内容列表
            list_alias_0 = read_content_alias_0.split('\n')

            # 新建词典, 以:分割,冒号的人名为key,冒号后的别名列表eval为value.
            dct_alias_0 = {}
            for list_alias_0_t0 in list_alias_0:
                """
                $1 index_of_split                                               查找':'的下标
                $2 dict_alias_0_key                                             从0下标截取到':'处,即人名
                $3 dict_alias_0_value                                           第一个|后内容,即别名表
                $4 dct_alias_0[dict_alias_0_key] = dict_alias_0_value           更新字典
                """
                index_of_split = list_alias_0_t0.find(':')
                dict_alias_0_key = list_alias_0_t0[0:index_of_split]
                dict_alias_0_value = list_alias_0_t0[list_alias_0_t0.find('|')+1:]
                dct_alias_0[dict_alias_0_key] = dict_alias_0_value

            # 使用t2遍历字典的键, 使用正则表达式替换别名
            for list_alias_0_t2 in list(dct_alias_0.keys()):
                read_content_pure_0 = re.sub(
                    dct_alias_0[list_alias_0_t2], list_alias_0_t2, read_content_pure_0)

        # 否则保持原文本内容, 另存为#file_03_alias.txt
        else:
            print("No alias in "+file_dir_0+", skipped")

        # 保存内容至$file_03_alias.txt文件
        open_file_alias_0 = open(file_source_name_0.replace(
            "_02_pure.txt", "_03_alias.txt"), 'w+', encoding='utf-8')
        open_file_alias_0.write(read_content_pure_0)
        open_file_alias_0.close()

    except Exception as identifier:
        print(file_source_name_0+" : "+identifier)
