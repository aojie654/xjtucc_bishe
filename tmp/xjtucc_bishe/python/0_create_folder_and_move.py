# encoding=utf-8

import os
import os.path as op

# Save the system type
system_type=os.uname().sysname

# Init the filename list
file_list = []

# Input the working folder
working_folder = input("Inputs the working folder please:")

# If system type is Windows, replace the '\' with '\\'
if system_type == "Windows":
    working_folder.replace("\\", "\\\\")

# Change the working folder
os.chdir(working_folder)
#os.chdir("D:\\tmp\\xjtucc_bishe\\create_folder")

# Walk in the working folder
walk_result = os.walk(".")

#
for i in walk_result:
    file_list.append(i)

for i in file_list[1:]:
    print(i)
