#!python3
# mcb.pyw - 将文本片段保存并加载到剪贴板。
# 用法：py.exe mcb.pyw save &lt;keyword> - 将剪贴板保存为关键字。
# py.exe mcb.pyw &lt;keyword> - 将关键字加载到剪贴板。
# py.exe mcb.pyw list - 将所有关键字加载到剪贴板。


import pyperclip
import sys
import shelve

shel_file = shelve.open("D:/Destok/MyGit/PythonLearning/plus/mcb")
# TODO: 保存剪贴板的内容
if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    shel_file[sys.argv[2]] = pyperclip.paste
if len(sys.argv) == 3 and sys.argv[1].lower() == "delete":
    if sys.argv[2] in shel_file.keys():
        del shel_file[sys.argv[2]]
        pyperclip.copy("删除成功!")
    else:
        pyperclip.copy("找不到关键字!")
elif len(sys.argv) == 2:
    # TODO: 列出关键字加载到剪贴板中
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(shel_file.keys())))
    elif sys.argv[1] in shel_file:
        pyperclip.copy(shel_file[sys.argv[1]])


shel_file.close()
