from os import system as s
from subprocess import getoutput as spgop
import re

# 输入路径
dir0 = "/Volumes/data/codes/xjtucc_bishe/znl/copy/中篇小说/"
# dir0 = input("Input DIR plz(with out end of /):")

# 调用find查找$file_utf8.txt文件
str0 = str(spgop("find "+dir0+" -name '*_utf8.txt'"))

# 定义列表l0以存放分割后的文件列表
l0 = str0.split('\n')
l1 = []

# 根据文件名去掉$file_utf8.txt创建作品名称列表
for t in l0:
    t = t.replace(dir0+"/", '')
    t = t.replace("_utf8.txt", '')
    t = t[0:t.find('/')]
    l1.append(t)

# 删除每个$file_utf8.txt中的广告,章节,作者和日期(冗余文字)
for t in l0:

    # 跳过已经去除冗余文字的文件
    if "_pure.txt" in t:
        pass
    else:
        try:

            # 读取文件内容
            tf0 = open(t, "r", encoding="utf-8")
            print(t)
            tr0 = tf0.read()
            tf0.close()
            
            # 创建/修改在原文件之后追加_pure的文本文件, 并保存为UTF-8编码
            tf0 = open(t.replace(".txt", '') +
                       "_pure.txt", "w+", encoding="utf-8")
            
            # 删除\u3000之类的不可编码字符
            tr0 = re.sub(r"u\\\d?", "", tr0)
            
            # 删除类似于广告之类的文本
            tr0 = re.sub(r"http[^\n]*?\n", "", tr0)
            tr0 = re.sub(r"欢迎下载更多小说", "", tr0)
            
            # 删除章节
            tr0 = re.sub(r"\s*[一二三四五六七八九十]{1,3}\n", "", tr0)
            tr0 = re.sub(
                r"(第.{1,3}[章节]|[作写]于|.{1,4}年.{1,2}月(.{1,2}日)*|.{1,2}月.{1,2}日)", "", tr0)
            
            # 删除作者和完稿地址
            tr0 = re.sub(r"(贾平凹.+|路遥.+)?全文完.*选自.+", "", tr0)
            tr0 = re.sub(r".*(初|毕|写)稿?于(改)*(再改于)*.+", "", tr0)
            
            # 保存并关闭文件
            tf0.write(tr0)
        except Exception as identifier:
            print(identifier)
        finally:
            tf0.close()
