#-*- coding：utf-8 -*-

from os import system as s, path as p
from subprocess import getoutput as spgop
import re
# 输入路径
# dir0 = input("Input DIR plz(with out end of /):")
dir0 = "/Volumes/data/tmp/midcopy/美穴地"

# 由于不是每个作品都有别名, 因此使用find查找alias.txt文件
find_result_0 = str(spgop("find "+dir0+" -name 'alias.txt'"))

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
        source_file_name_0 = file_dir_0+"/"+file_name_0+"_utf8_pure.txt"
        # 判断$file_whole.txt文件如果存在, 即已经处理过则跳过
        if p.exists(source_file_name_0.replace(".txt", "_whole.txt")):
            pass
        # 否则进行别名处理
        else:
            # 打开alias.txt,读取alias.txt内容, 将获取到的内容以换行进行分割得到内容列表
            open_file_alias_0 = open(list_file_name_0_t, 'r', encoding='utf-8')
            list_alias_0 = open_file_alias_0.read().split('\n')

            # 打开#file_pure.txt, 读取内容
            print(source_file_name_0)
            open_file_pure_0 = open(source_file_name_0, 'r', encoding='utf-8')
            read_content_0 = open_file_pure_0.read()

            # 去掉\n和多余空格, 即合并换行
            read_content_0 = re.sub(r'[\n\s]+', '', read_content_0)

            # 新建词典, 以:分割,冒号的人名为key,冒号后的别名列表eval为value.
            dct0 = {}
            for list_alias_0_t0 in list_alias_0:
                """
                $1 list_alias_0_t0.find(':')                            查找':'的下标
                $2 list_alias_0_t0[0:$1]                                从0下标截取到':'处,即人名
                $3 dct0[$2]                                             更新值为value的人名
                $4 list_alias_0_t0.find(':')+1:]                        冒号后内容
                $5 re.sub(r"\[|,?\]", "", $4)                           将'['',]'']'删除,直至$4包含','
                $6 $5.split(',')                                        使用','分割各别名,即得到别名列表
                """
                dct0[list_alias_0_t0[0:list_alias_0_t0.find(
                    ':')]] = re.sub(r"\[|,?\]", "", list_alias_0_t0[list_alias_0_t0.find(':')+1:]).split(',')

            # 使用t2遍历字典的键
            list_person_names_0 = list(dct0.keys())
            for list_alias_0_t2 in list_person_names_0:
                # 使用t3遍历字典的值
                list_person_alias_0 = list(dct0[list_alias_0_t2])[1:]
                for list_alias_0_t3 in list_person_alias_0:
                    # 使用key替换values, 即人名替换别名
                    read_content_0 = read_content_0.replace(
                        list_alias_0_t3, list_alias_0_t2)
                
            open_file_whole_0 = open(source_file_name_0.replace(
                ".txt", "_whole.txt"), 'w+', encoding='utf-8')
            open_file_whole_0.write(read_content_0)
    except Exception as identifier:
        print(identifier)
    finally:
        open_file_alias_0.close()
        open_file_pure_0.close()
        open_file_whole_0.close()
