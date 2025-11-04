#!usr/bin/python3
# -*- coding: utf-8 -*-
import os
import send2trash
from pathlib import Path

def delete_rubbish(folder='.', extname='.url'):
    paths = []
    for root, subfolders, files in os.walk(folder):
        for file in files:
            if file.endswith(extname):
                path = Path(root, file)
                paths.append(path)
    if (paths):
        for path in paths:
            print('To be deleted: ', path)
        choice = input('是否删除以上文件(y/n)?\n')
        if choice.lower() == 'y':
            print('删除以上文件')
            for path in paths:
                send2trash.send2trash(path)
        elif choice.lower() == 'n':
            print('保留以上文件')
        else:
            print('未做处理')
    else:
        print('未找到文件')

    print('处理完毕')

folder = Path(input(r'输入目标文件夹路径： 例如：D:\test''\n'))
extname = input(r'输入要删除的文件的扩展名： 例如： .xml''\n')
delete_rubbish(folder, extname)
os.system('pause')
