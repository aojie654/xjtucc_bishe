# encoding=utf-8
"""
根据文本名称创建相应的文件夹
"""

import os
import shutil


def folder_content(folder_path):
    """
    获取文件夹目录树
    """

    # 列出当前目录内容
    filepath_content = os.listdir()

    # 排除 macOS 中的 .DS_Store 文件
    if ".DS_Store" in filepath_content:
        filepath_content.remove(".DS_Store")

    # 返回目录文件
    return filepath_content


def create_folders(file_name):
    """
    创建文件夹
    """

    # 将文件名中的 .txt 去掉, 得到相应的文件夹名
    texted_folder_name = file_name.replace(".txt", "")
    message_return = ""

    try:
        # 判断文件夹是否已经创建:
        if not os.path.exists(texted_folder_name):
            # 文件夹不存在时, 创建相对应文件夹
            os.mkdir(texted_folder_name)
            message_folder = "文件夹: " + texted_folder_name + " 创建成功"
        else:
            # 否则跳过创建
            message_folder = "文件夹: " + texted_folder_name + " 已存在, 跳过创建"

        # 尝试移动文件
        shutil.move(file_name, texted_folder_name)
        message_moved = "文件: " + file_name + " 移动完毕"

        # 拼接 文件夹创建信息 和 文件移动信息
        message_return = message_folder + "\n" + message_moved
    except Exception as identifier:
        message_return = "捕获到了一个其他异常, 相关信息为:" + str(identifier)

    return message_return


def mkdir_move():
    """
    创建文件夹并移动文件的全部流程
    """
    # 输入需要根据txt文件名创建文件夹的路径
    path_text = input("请输入存放 txt 文件的目录(Windows需要用\"\\\\\"将\"\\\"自身转义): ")
    # path_text = "/Volumes/data/tmp/python_debug/p3/xjtucc_bishe/00_origin_work/中篇00"

    # 改变工作路径
    os.chdir(path_text)

    # 调用 folder_content() 得到当前工作目录的目录树
    list_folder = folder_content('.')

    # 针对每个文件分循环调用 create_folders() 创建文件夹
    for file_name in list_folder:
        # 对每个文件名进行校对, 如果属于 txt 文件则调用 create_folders() 创建名称对应的文件夹
        if os.path.splitext(file_name)[1] == ".txt":
            # 获取返回信息并输出
            message_call = create_folders(file_name)
        else:
            # 如果没有文本文件, 则无需执行任何动作
            message_call = os.path.abspath(file_name) + " 不是 txt 文件, 跳过创建"

        # 输出结果信息
        print(message_call)

    # 输出执行结束提示
    message_final = "脚本执行完毕."

    # 返回最终执行结果
    return message_final


if __name__ == "__main__":
    message_process = mkdir_move()
    print(message_process)
