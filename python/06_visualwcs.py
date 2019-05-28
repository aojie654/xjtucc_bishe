# -*- coding: utf-8 -*-

from os import system as s, path as p
from subprocess import getoutput as spgop
from matplotlib import pyplot as plt
import matplotlib
from matplotlib.font_manager import findfont, FontProperties
from wordcloud import wordcloud as wc


# 输入路径
# dir0 = input("Input DIR plz(with out end of /):")
dir0 = "/Users/aojie654/tmp/sja/text/中篇"

# 调用find查找$file_05_departs.txt文件
find_command_0 = "find "+dir0+" -name '*_05_departs.txt'"
find_result_0 = spgop(find_command_0)

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
    print(file_dir_0+", ", end="")

    # 欲保存的文件名
    file_save_name_0 = file_dir_0+"/"+work_name_0+"_06_wordclouds.png"

    try:
        # 判断$file_06_visualbars.png文件如果存在, 即已经处理过则跳过
        if p.exists(file_save_name_0):
            print("[Skipped.]")
            continue
        print("[Processing...]")

        # 打开$file_05_departs.txt文件进行读取,以行分割为列表
        open_source_content_0 = open(file_source_name_0, "r")
        read_source_content_0 = open_source_content_0.read()
        open_source_content_0.close()

        # 词云生成,需要设置字体为文泉驿米黑
        word_cloud_0 = wc.WordCloud(font_path="/Users/aojie654/Library/Fonts/wqy-microhei.ttc", width=1100, height=500).generate(read_source_content_0)

        # 设置字体为苹方
        plt.rcParams['font.sans-serif'] = ['PingFang HK']

        # 设置标题
        plt.title(work_name_0+"词云")

        # 词云展示并存储
        plt.imshow(word_cloud_0)
        plt.axis("off")
        # plt.show()
        print(file_save_name_0+" saving...")
        plt.savefig(file_save_name_0)
    except Exception as identifier:
        print(file_source_name_0+" : "+identifier)
