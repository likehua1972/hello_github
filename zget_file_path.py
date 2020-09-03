import os
import tkinter as tk
from tkinter import filedialog

def get_file_path():
    """
    通过tkinter窗体
    获取指定文件夹的路径，用于保存相关的文件
    :return: 文件夹路径
    """
    try:
        root = tk.Tk()
        root.withdraw()
        directory_path = filedialog.askdirectory()
    except Exception as e:
        print(e)
    return directory_path

if __name__=='__main__':
    file_path=get_file_path()
    print(file_path)