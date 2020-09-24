# encoding=utf-8
"""
依赖包: chardet

将文本转换为 utf-8 编码
"""

import os
import chardet


def content_purly(filename, filname_save, encodes):
    """
    去冗余内容
    """
    try:
        # 定义文本保存的编码格式
        filename_source_encode_convert = filename
        filename_save_encode_convert = filname_save

        chardet_source = encodes
        chardet_result = "utf-8"

        # 以猜测出的编码读取文本内容, 并忽略出错的字符, 关闭文件
        object_open_source = open(filename_source_encode_convert, "r",
                                  encoding=chardet_source, errors="ignore")
        content_open_source = object_open_source.read()
        object_open_source.close()

        # 创建添加了 _01_utf8 的文本文件
        object_open_save = open(
            filename_save_encode_convert, "w+", encoding=chardet_result)
        object_open_save.write(content_open_source)
        object_open_save.close()

        # 返回处理成功信息
        result_encode_convert = "文件: " + filename_save_encode_convert + " 保存成功"

    except Exception as identifier:

        # 返回异常信息
        result_encode_convert = "文件: " + filename_save_encode_convert + \
            " 处理过程中出现了一个异常, 详细信息为: \n" + str(identifier)

    # 返回处理结果
    return result_encode_convert


def get_folder_tree(folder_path):
    """
    获取 folder_path 的目录树
    """

    # 尝试获取目录树
    try:
        # 更改工作目录
        os.chdir(folder_path)

        # 获取当前目录里的文件
        folder_path_content = os.listdir(".")

        # 排除 .DS_Store 文件
        if ".DS_Store" in folder_path_content:
            folder_path_content.remove(".DS_Store")

        # 返回目录树
        return folder_path_content
    except FileNotFoundError as identifier:
        print("路径: " + folder_path + " 不存在")
    except PermissionError as identifier:
        print("路径: " + folder_path + " 无访问权限")
    except Exception as identifier:
        print("捕获到一个异常, 详细信息为: " + str(identifier))


def detect_convert(filename):
    """
    检测文件编码并转换为utf-8格式
    """

    try:
        # 获取源文件的编码方式
        filename_source_detect_convert = filename
        filename_save_detect_convert = filename_source_detect_convert.replace(
            ".txt", "_01_utf8.txt")
        encodes = encode_detect(filename_source_detect_convert)

        if ("_01_utf8" in filename_source_detect_convert) or (os.path.exists(filename_save_detect_convert)):
            result_detect_convert = "文件: " + filename_save_detect_convert + " 已存在, 跳过处理"
        else:
            # 如果编码格式不是 utf-8, 在进行文件格式转换
            print("文件: " + filename + " 为 " + encodes + " 编码, ", end="")
            if encodes != "utf-8":
                print("开始转换")
            else:
                print("仅复制并重命名")
            result_detect_convert = encode_convert(filename_source_detect_convert, filename_save_detect_convert, encodes)
    except Exception as identifier:
        result_detect_convert = "文件: " + filename + \
            " 处理过程中产生了一个异常, 详细信息为: " + str(identifier)

    # 返回处理结果
    return result_detect_convert


def process_start(folder_path):
    """
    开始处理文件
    """
    try:
        # 获取目录内容
        folder_path_content = get_folder_tree(folder_path)

        # 遍历每一个子文件夹, 即与文本文件名对应的文件夹
        for folder_path_single in folder_path_content:

            # 列出子文件夹中的文件
            folder_path_content_single = os.listdir(folder_path_single)

            # 如果文件夹中包含 .DS_Store, 则排除掉该文件
            if ".DS_Store" in folder_path_content_single:
                folder_path_content_single.remove(".DS_Store")

            # 获取当前目录的绝对路径
            folder_path_single_abs = os.path.abspath(folder_path_single)

            # 通过join命令将目录绝对路径和文件名拼接的到绝对路径
            filename = os.path.join(
                folder_path_single_abs, folder_path_content_single[0])

            # 判断文件正确性, 并调用 detect_convert() 进行编码转换
            if os.path.splitext(filename)[1] == ".txt":
                result_detect_convert = detect_convert(filename)
            else:
                result_detect_convert = filename + " 不是一个 txt 文本文档"

            # 输出处理信息
            print(result_detect_convert)

        # 文件夹正常处理提示
        result_process = "文件夹: " + folder_path + "处理完毕"

    except Exception as identifier:
        # 文件夹异常信息提示
        result_process = "处理过程中发生异常, 详细信息为: " + str(identifier)

    # 返回处理结果信息
    return result_process


if __name__ == "__main__":

    input_hint = """请输入需要去冗余内容的文本的上级路径. 
例如, 需要处理的文本为 \"/home/txt/中篇/天狗/天狗.txt\"
则输入 /home/txt/中篇
    """

    print(input_hint)
    # folder_path = input("请输入: ")
    folder_path = "/Volumes/data/tmp/python_debug/p3/xjtucc_bishe/00_origin_work/中篇01"

    # 调用 process_start() 进行开始处理
    result_process_final = process_start(folder_path)

    # 输出转换结果
    print(result_process_final)
