from os import system as s
from subprocess import getoutput as spgop
import re

# 输入路径
# dir0 = "/Users/aojie654/tmp/bishe_znl/textcopy"
dir0 = input("Input DIR plz(with out end of /):")

# 追加/
dir1 = dir0+'/'

# 调用find查找.txt文件
str0 = str(spgop("find "+dir0+" -name '*.txt'"))

# 定义列表l0以存放分割后的文件列表
l0 = str0.split('\n')

# 删除每个$file_rex.txt中的标点和空字符
for t in range(0, len(l0)):
    # 如果文件名中包含_rex，跳过循环
    if "_rex" in l0[t]:
        continue
    else:
        # 以GB2312读取文件内容
        # tf0 = open(l0[t], "r", encoding="utf-8")
        tf0 = open(l0[t], 'r', encoding='GB2312', errors='ignore')
        print(l0[t])
        tr0 = tf0.read()
        try:
            # 创建/修改在原文件之后追加_rex的文本文件, 并保存为UTF-8编码
            tf0 = open(l0[t].replace(".txt", '') +
                       "_rex.txt", "w+", encoding="utf-8")

            # 采用正则表达式替换标点
            tr0 = re.sub(r"u\\\d?", "", tr0)
            tr0 = re.sub(r"欢迎下载更多小说", "", tr0)
            tr0 = re.sub(r"http[^\n]*?\n", "", tr0)
            tr0 = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fa5]", "", tr0)
            tr0 = re.sub(
                r"(第.{1,3}[章节]|[作写]于|.{1,4}年.{1,2}月(.{1,2}日)*|.{1,2}月.{1,2}日)", "", tr0)
            tr0 = re.sub(r"(贾平凹.+)?全文完.*选自.+", "", tr0)

            # 保存并关闭文件
            tf0.write(tr0)
        except Exception as identifier:
            print(identifier)
        finally:
            tf0.close()
