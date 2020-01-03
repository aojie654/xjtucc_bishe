# encoding=utf-8

import os
import os.path as op

file_list = []
os.chdir("D:\\tmp\\xjtucc_bishe\\create_folder")
walk_result = os.walk(".")

for i in walk_result:
    file_list.append(i)

for i in file_list[1:]:
    print(i)
