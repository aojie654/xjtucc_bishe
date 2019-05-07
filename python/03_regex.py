from os import system as s
from subprocess import getoutput as spgop
import re

# 输入路径
dir0 = "/Volumes/data/codes/xjtucc_bishe/znl/copy/中篇小说/人生"
# dir0 = input("Input DIR plz(with out end of /):")

# 追加/
dir1 = dir0+'/'

# 调用find查找.txt文件
str0 = str(spgop("find "+dir0+" -name '*.txt'"))

# 定义列表l0以存放分割后的文件列表
l0 = str0.split('\n')

# 删除每个$file_rex.txt中的标点和空字符
for t in l0:
    # 如果文件名中包含_rex，跳过循环
    if "_rex" in t:
        continue
    else:
        try:
            # 创建/修改在原文件之后追加_rex的文本文件, 并保存为UTF-8编码
            tf0 = open(t.replace(".txt", '') +
                       "_rex.txt", "w+", encoding="utf-8")
            # 删除\u3000之类的不可编码字符
            tr0 = re.sub(r"u\\\d?", "", tr0)
            # 删除类似于广告之类的文本
            tr0 = re.sub(r"http[^\n]*?\n", "", tr0)
            tr0 = re.sub(r"欢迎下载更多小说", "", tr0)
            # # 采用正则表达式替换标点
            # tr0 = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fa5]", "", tr0)
            tr0 = re.sub(
                r"(第.{1,3}[章节]|[作写]于|.{1,4}年.{1,2}月(.{1,2}日)*|.{1,2}月.{1,2}日)", "", tr0)
            tr0 = re.sub(r"(贾平凹.+|路遥.+)?全文完.*选自.+", "", tr0)
            tr0 = re.sub(r".*(初|毕)稿于.+(改.*)*(再改于*)*", "", tr0)

            # 保存并关闭文件
            tf0.write(tr0)
        except Exception as identifier:
            print(identifier)
        finally:
            tf0.close()
