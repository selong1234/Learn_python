import os
from pathlib import Path
def del_files(path, extname):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(extname):  # 指定要删除的格式，这里是jpg 可以换成其他格式
                os.remove(Path.join(root, name))
                print("Delete File: " + Path.join(root, name))
    
    
folder = input(r'输入目标文件夹： 例如：D:\\test''\n')
extname = input(r'输入要删除的文件的扩展名： 例如： .xml''\n')
del_files(folder, extname)
os.system('pause')