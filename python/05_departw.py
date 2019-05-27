# -*- coding: utf-8 -*-

from os import system as s, path as p
from subprocess import getoutput as spgop
import jieba
import jieba.posseg as pseg

# 输入路径
dir0 = input("Input DIR plz(with out end of /):")

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
                "_04_whole.txt", "_05_departw.txt")) and p.exists(file_source_name_0.replace(
                "_04_whole.txt", "_05_markw.txt")):
            print("[Skipped.]")
        else:
            print("[Processing...]")

            # 拼接以得到dict.txt绝对路径
            file_dict_name_0 = file_dir_0+"/dict.txt"

            # 加载字典
            if p.exists(file_dict_name_0):
                jieba.load_userdict(file_dict_name_0)
            else:
                pass

            # 打开$file_04_whole.txt, 读取文件内容并关闭文件
            file_open_alias_0 = open(file_source_name_0, 'r', encoding='utf-8')
            read_content_alias_0 = file_open_alias_0.read()
            file_open_alias_0.close()

            # 使用jieba进行精确分词
            result_jieba_0 = jieba.cut(read_content_alias_0, cut_all=False)

            # 将结果转换为文本
            result_depart_0 = " ".join(result_jieba_0)

            # 打开$file_05_departw.txt进行写入并关闭文件
            file_open_depart_0 = open(file_source_name_0.replace(
                "_04_whole.txt", "_05_departw.txt"), "w+", encoding="utf-8")
            file_open_depart_0.write(result_depart_0)
            file_open_depart_0.close()

            # 使用jieba进行磁性标注
            result_jieba_0 = pseg.cut(read_content_alias_0)

            # 打开$file_05_markw.txt写入标注结果
            file_open_mark_0 = open(file_source_name_0.replace(
                "_04_whole.txt", "_05_markw.txt"), "w+", encoding="utf-8")
            for word, flag in result_jieba_0:
                file_open_mark_0.write(str(word)+" "+str(flag)+"\n")
            file_open_mark_0.close()

    except Exception as identifier:
        print(file_source_name_0+" : "+identifier)
