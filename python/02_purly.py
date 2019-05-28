# -*- coding: utf-8 -*-

from os import system as s, path as p
from subprocess import getoutput as spgop
import re

# 输入路径
dir0 = input("Input DIR plz(with out end of /):")

# 调用find查找$file_01_utf8.txt文件
find_result_0 = spgop("find "+dir0+" -name '*_01_utf8.txt'")

# 定义列表list_file_name_0以存放分割后的文件列表
list_file_name_0 = find_result_0.split('\n')

# 遍历文件列表
for list_file_name_0_t in list_file_name_0:

    # 获取当前文件所在路径
    file_dir_0 = list_file_name_0_t[0:list_file_name_0_t.rfind('/')]

    # 获取作品名
    file_name_0 = file_dir_0[file_dir_0.rfind('/')+1:]

    # 文件源即为当前遍历元素
    file_source_name_0 = list_file_name_0_t
    print(file_source_name_0+", ", end="")
    
    # 跳过已经去除冗余文字的文件
    if p.exists(file_source_name_0.replace("_01_utf8.txt", "_02_pure.txt")):
        print("[Skipped.]")
        continue
    print("[Processing...]")
    try:
        # 读取文件内容
        open_file_source_0 = open(
            file_source_name_0, "r", encoding="utf-8")
        read_content_utf8_0 = open_file_source_0.read()

        # 创建_02_pure的文本文件, 并保存为UTF-8编码
        open_file_pure_0 = open(file_source_name_0.replace("_01_utf8.txt", '') +
                                "_02_pure.txt", "w+", encoding="utf-8")

        # 删除类似于广告之类的文本
        read_content_utf8_0 = re.sub(r"http[^\n]*?\n", "\n", read_content_utf8_0)
        read_content_utf8_0 = re.sub(
            r".*(更多小说|更多电子书|章节内容开始|内容简介).*", "", read_content_utf8_0)

        # 删除作者和摘录
        read_content_utf8_0 = re.sub(
            r".*(贾平凹.+|路遥.+)?.{1,10}(全文完|已完结).*(选自)?.{1,10}", "", read_content_utf8_0)

        # 删除开头作品名
        read_content_utf8_0 = re.sub(
            r"^(\s*《?)"+file_name_0+".{0,3}(贾平凹|路遥)?.{0,3}", "", read_content_utf8_0)

        # 删除章节
        read_content_utf8_0 = re.sub(
            r"(\n\s*[一二三四五六七八九十0-9]{1,3}\s*\n|.*第.{1,3}[章节部].*\s*)", "\n", read_content_utf8_0)

        # 删除时间和地址
        read_content_utf8_0 = re.sub(
            r"(到?(\s*.{1,4}年(.{1,3}月)?(.{1,3}日)?[写作初毕草改再]稿?于.{1,5}){1,3}\n)|((\s*[写作初毕草改再]稿?于.{1,4}年(.{1,3}月)?(.{1,3}日)?.{0,5}){1,3}\n)|(\s*.{1,4}年(.{1,3}月)?(.{1,3}日)?[早午晚夜初记春夏秋冬]?.{1,5}){1,2}\n", "\n", read_content_utf8_0)
        
        # 在文本末尾追加一个换行,便于删除写作时间等冗余信息
        read_content_utf8_0 = read_content_utf8_0 + "\n"

        # 删除两个以上的换行和行首空格
        read_content_utf8_0 = re.sub(r"(\n{2,}|\s+\n)", "\n", read_content_utf8_0)
        read_content_utf8_0 = re.sub(r"\n\s+", "\n", read_content_utf8_0)
        
        # 保存并关闭文件
        open_file_pure_0.write(read_content_utf8_0)
        open_file_source_0.close()
        open_file_pure_0.close()
    except Exception as identifier:
        print(identifier)
