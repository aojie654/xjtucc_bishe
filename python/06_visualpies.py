# -*- coding: utf-8 -*-

from os import system as s, path as p
from subprocess import getoutput as spgop
from matplotlib import pyplot as plt
import matplotlib
from matplotlib.font_manager import findfont, FontProperties


# 输入路径
# dir0 = input("Input DIR plz(with out end of /):")
dir0 = "/Users/aojie654/tmp/sja/text/中篇"

# 调用find查找$*_05_marks.txt文件
find_result_0 = spgop("find "+dir0+" -name '*_05_marks.txt'")

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
    file_save_name_0 = file_dir_0+"/"+work_name_0+"_06_visualpies.png"

    try:
        # 判断$file_06_visualpies.png文件如果存在, 即已经处理过则跳过
        if p.exists(file_save_name_0):
            print("[Skipped.]")
            continue
        print("[Processing...]")

        # 打开*_05_marks.txt文件进行读取,以行分割为列表
        open_fre_content_0 = open(file_source_name_0, "r")
        read_fre_content_0 = open_fre_content_0.read()
        open_fre_content_0.close()
        
        # 将文本以回车分割为列表
        list_fre_line_0 = read_fre_content_0.split("\n")
        
        # 新建类型表和词频字典
        dct_type_fre_0 = {}
        
        # 遍历前20个出现频率最高的词,跳过包含列名的第一行
        for tmp_of_list_fre_line in list_fre_line_0:
            if (tmp_of_list_fre_line==""):
                continue
            
            # 将每行以" "分割,得到列表
            tmp_of_fre_line_split = tmp_of_list_fre_line.split(" ")
            
            # 取出词(下标为1),出现次数(下标为2)
            tmp_word_0 = tmp_of_fre_line_split[1]
            tmp_fre_0 = int(tmp_of_fre_line_split[1].replace(" ", ""))
            if (len(tmp_word_0) != 1) and (tmp_word_0 in read_stop_content_0):
                # 将词追加与词列表之后, 将出现次数(下标为2)追加于词频列表之后
                list_type_0.append(tmp_word_0)
                list_type_fre_0.append(tmp_fre_0)
            if len(list_type_0) >= 20:
                break
        
        # 设置字体为苹方,字体大小为4, 分辨率为900 * 1000
        plt.rcParams['font.sans-serif'] = ['PingFang HK']
        plt.rcParams['font.size'] = 4
        plt.rcParams['figure.figsize'] = (4.5, 5)
        plt.rcParams['savefig.dpi'] = 200
        plt.rcParams['figure.dpi'] = 200

        # 设置标题
        plt.title("《"+work_name_0+"》"+"词类型词频统计")

        # 设置横轴为人名, 纵轴为数量
        plt.pie(list_type_0, list_type_fre_0)
        # plt.show()
        print(file_save_name_0+" saving...")
        plt.savefig(file_save_name_0)
    except Exception as identifier:
        print(file_source_name_0+" : "+identifier)
