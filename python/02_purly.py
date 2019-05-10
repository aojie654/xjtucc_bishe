# -*- coding：utf-8 -*-


from os import system as s
from subprocess import getoutput as spgop
import re

# 输入路径
dir0 = input("Input DIR plz(with out end of /):")

# 调用find查找$file_utf8.txt文件
find_result_0 = str(spgop("find "+dir0+" -name '*_utf8.txt'"))

# 定义列表list_file_name_0以存放分割后的文件列表
list_file_name_0 = find_result_0.split('\n')

# 删除每个$file_utf8.txt中的广告,章节,作者和日期(冗余文字)
for list_file_name_0_t in list_file_name_0:

    # 输出文件名
    print(list_file_name_0_t, end=", ")
    
    # 跳过已经去除冗余文字的文件
    if "_pure.txt" in list_file_name_0_t:
        print("[Skiped.]")
    else:
        print("[Processing...]")
        try:
            # 读取文件内容
            open_file_source_0 = open(
                list_file_name_0_t, "r", encoding="utf-8")
            read_content_0 = open_file_source_0.read()

            # 创建/修改在原文件之后追加_pure的文本文件, 并保存为UTF-8编码
            open_file_pure_0 = open(list_file_name_0_t.replace(".txt", '') +
                                    "_pure.txt", "w+", encoding="utf-8")

            # 删除类似于广告之类的文本
            read_content_0 = re.sub(r"http[^\n]*?\n", "\n", read_content_0)
            read_content_0 = re.sub(
                r".*(更多小说|更多电子书|章节内容开始|内容简介).*", "", read_content_0)

            # 删除作者和摘录
            read_content_0 = re.sub(
                r".*(贾平凹.+|路遥.+)?.{1,10}(全文完|已完结).*(选自)?.{1,10}", "", read_content_0)

            # 删除开头作品名
            list_file_name_0_t = list_file_name_0_t.replace(dir0+"/", '')
            list_file_name_0_t = list_file_name_0_t.replace("_utf8.txt", '')
            if '/' in list_file_name_0_t:
                works_name_0 = list_file_name_0_t[list_file_name_0_t.rfind(
                    '/')+1:]
            else:
                works_name_0 = list_file_name_0_t
            read_content_0 = re.sub(
                r"^.{0,3}"+works_name_0+".*(贾平凹|路遥)?.*", "", read_content_0)

            # 删除章节
            read_content_0 = re.sub(
                r"(^\s*[一二三四五六七八九十0-9]{1,3}\s*\n|.*第.{1,3}[章节部].*\s*)", "\n", read_content_0)

            # 删除时间和地址
            read_content_0 = re.sub(
                r"(.+年.+[写作初毕]稿?于.{1,10}\n)|([写作毕初]稿?于.{1,4}年(.{1,3}月)?(.{1,3}日)?).{0,10}\n|(.+年(.{1,3}月)?(.{1,3}日)?[早午晚夜初记]?.{1,10}\n)", "\n", read_content_0)
            
            # 删除两个以上的换行和行首空格
            read_content_0 = re.sub(r"(\n{2,}|\s+\n)", "\n", read_content_0)
            read_content_0 = re.sub(r"\n\s+", "\n", read_content_0)
            
            # 保存并关闭文件
            open_file_pure_0.write(read_content_0)
        except Exception as identifier:
            print(identifier)
        finally:
            open_file_source_0.close()
            open_file_pure_0.close()
