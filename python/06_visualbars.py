# -*- coding: utf-8 -*-

from os import system as s, path as p
from subprocess import getoutput as spgop
from matplotlib import pyplot as plt
import matplotlib
from matplotlib.font_manager import findfont, FontProperties


# 输入路径
# dir0 = input("Input DIR plz(with out end of /):")
dir0 = "/Users/aojie654/tmp/sja/text/中篇/白朗"

# 调用find查找$frequency.csv文件
find_result_0 = spgop("find "+dir0+" -name 'frequency.csv'")

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
    file_save_name_0 = file_dir_0+"/"+work_name_0+"_06_visualbars.png"

    try:
        # 判断$file_06_visualbars.png文件如果存在, 即已经处理过则跳过
        if p.exists(file_save_name_0):
            print("[Skipped.]")
        else:
            print("[Processing...]")

            # 打开frequency.csv文件进行读取,以行分割为列表
            open_fre_content_0 = open(file_source_name_0, "r")
            read_fre_content_0 = open_fre_content_0.read()
            open_fre_content_0.close()

            # 读取前20个词频最高的词
            list_fre_line_0 = read_fre_content_0.split("\n")[1:21]

            # 新建词列表和词频列表
            list_words_0, list_word_fre_0 = [], []

            # 遍历前20个出现频率最高的词
            for tmp_of_list_fre_line in list_fre_line_0:

                # 将每行以"\t"分割,得到列表
                tmp_of_fre_line_split = tmp_of_list_fre_line.split("\t")

                # 将词(下标为1)追加与词列表之后, 将出现次数(下标为2)追加于词频列表之后
                list_words_0.append(tmp_of_fre_line_split[1])
                list_word_fre_0.append(
                    int(tmp_of_fre_line_split[2].replace(" ", "")))

            # 输出词列表和词频列表
            print(str(list_words_0)+"\n"+str(list_word_fre_0))
            
            # 设置字体为苹方,字体大小为4, 分辨率为1200 * 600
            plt.rcParams['font.sans-serif'] = ['PingFang HK']
            plt.rcParams['font.size'] = 4
            plt.rcParams['figure.figsize'] = (6, 3)
            plt.rcParams['savefig.dpi'] = 200
            plt.rcParams['figure.dpi'] = 200

            # 设置标题
            plt.title(work_name_0+"出现最高词汇统计")

            # 设置横轴为人名, 纵轴为数量
            plt.bar(list_words_0, list_word_fre_0)
            # plt.show()
            print(file_save_name_0+" saving...")
            plt.savefig(file_save_name_0)
    except Exception as identifier:
        print(file_source_name_0+" : "+identifier)
