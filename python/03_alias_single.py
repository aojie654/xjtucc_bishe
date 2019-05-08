from os import system as s
from subprocess import getoutput as spgop
import re

# 输入路径
dir0 = input("Input DIR plz(with out end of /):")

# 调用find查找$file_pure.txt文件
str0 = str(spgop("find "+dir0+" -name '*_pure.txt'"))

# 定义列表l0以存放分割后的文件列表
l0 = str0.split('\n')

# 删除每个$file_pure.txt中的广告,章节,作者和日期(冗余文字)
for t in l0:
    # 获取当前文件所在路径
    dt0 = t[0:t.rfind('/')]

    # 读取alias.txt内容
    try:
        tf0 = open(dt0+'/alias.txt', 'r', 'utf-8')

        # 将获取到的内容以换行进行分割得到内容列表
        ct0 = tf0.read().split('\n')
        
        # 新建词典, 以:分割,冒号的人名为key,冒号后的别名列表eval为value.
        dct0 = {}
        for t in ct0:
            """
            t.find(':')                     查找:所处下标
            t[0:t.find(':')]                截取0到:处,即人名
            dct0[t[0:t.find(':')]]          更新key为人名的键值对
            t.find(':')+2:-1]               取方括号内的字符串
            t[t.find(':')+2:-1].split(',')  使用','分割,即得到别名列表
            """
            dct0[t[0:t.find(':')]] = t[t.find(':')+2:-1].split(',')


    except Exception as identifier:
        print(identifier)
    finally:
        tf0.close
    # 跳过已经去除冗余文字的文件
    if "_single.txt" in t:
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
                       "_single.txt", "w+", encoding="utf-8")

            # 删除\u3000之类的不可编码字符
            tr0 = re.sub(r"u\\\d?", "", tr0)

            # 删除类似于广告之类的文本
            tr0 = re.sub(r"http[^\n]*?\n", "", tr0)
            tr0 = re.sub(r".*(更多小说|更多电子书|章节内容开始|内容简介).*", "", tr0)

            # 删除开头作品名
            t = t.replace(dir0+"/", '')
            t = t.replace("_pure.txt", '')
            if '/' in t:
                an0 = t[t.rfind('/'):]
            else:
                an0 = t
            rt0 = re.compile(r".{0,3}"+an0+".*(贾平凹|路遥)?.*")
            tr0 = re.sub(rt0, "", tr0)

            # 删除章节
            tr0 = re.sub(
                r"(\s*[一二三四五六七八九十]{1,3}\s*\n|第.{1,3}[章节]\s*)", "", tr0)

            # 删除时间和地址
            tr0 = re.sub(
                r"(.+年.+[写作初毕]稿?于.+)|([写作毕初]稿?于.{1,4}年(.{1,3}月)?(.{1,3}日)?).{0,10}|(.+年(.{1,3}月)?(.{1,3}日)?[早午晚夜初记]?.{1,10})", "", tr0)

            # 删除作者和摘录
            tr0 = re.sub(r".*(贾平凹.+|路遥.+)?(全文完|已完结).*(选自)?.+", "", tr0)

            # 保存并关闭文件
            tf0.write(tr0)
        except Exception as identifier:
            print(identifier)
        finally:
            tf0.close()
