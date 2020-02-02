# encoding=utf-8
"""
这个模块用于根据文本名称创建相应的文件夹
"""

import os
from platform import system as os_system


def folder_tree(folder_path):
    """
    获取文件夹目录树
    """

    # os_walker = os.walk(path_text)

    # # 将迭代器中的每个对象保存至列表
    # list_folder = []
    # for generator_tmp in os_walker:
    #     # 在macOS中排除 .DS_Store 文件
    #     generator_tmp[2].remove(".DS_Store")

    #     # 将目录对象添加至列表中
    #     list_folder.append(generator_tmp)

    # 
    list_folder = os.listdir()

    # 排除 macOS 中的 .DS_Store 文件
    list_folder.remove(".DS_Store")

    # 返回目录文件
    return list_folder


def create_folders(file_name):
    """
    创建文件夹
    """

    # 将文件名中的 .txt 去掉, 得到相应的文件夹名
    texted_folder_name = file_name.replace(".txt", "")

    try:
        os.mkdir(texted_folder_name)
    except FileExistsError as identifier:
        print("文件夹"+ texted_folder_name +"已经存在")
    except Exception as identifier:
        print("捕获到了一个其他异常, 相关信息为:" + str(identifier))
    else:
        print(texted_folder_name + " 创建成功")
    


if __name__ == "__main__":
    # 输入需要根据txt文件名创建文件夹的路径
    # path_text = input("Input DIR plz(with out end of /):")
    path_text = "/Volumes/data/tmp/python_debug/p3/xjtucc_bishe/00_origin_work/中篇"

    # 改变工作路径
    os.chdir(path_text)

    # 调用 folder_tree() 得到当前工作目录的目录树
    list_folder = folder_tree('.')

    # 目录树中每个文件文件分别进行创建目录
    # for file_name in list_folder[-1][-1]:
    #     # 对每个文件名进行校对, 如果包含 .txt 则调用 create_folders() 创建名称对应的文件夹
    #     if ".txt" in file_name:
    #         create_folders(file_name)

    for file_name in list_folder:
        # 对每个文件名进行校对, 如果包含 .txt 则调用 create_folders() 创建名称对应的文件夹
        if ".txt" in file_name:
            create_folders(file_name)
