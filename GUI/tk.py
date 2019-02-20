#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import tkinter
import tkinter.messagebox as messagebox
import requests
# import re

# req  = requests.get('http://v.huya.com/g/vhuyajdqs?set_id=4&order=hot&page=1')
# # html = requests.get("http://www.baidu.com")

# v = re.findall(r'(?<=data-original=").*?(?=")', req.text)
# for item in v:
#     t = re.findall(r'(?<=/)\d{9}(?=/)', item)
#     print(t[0])

# <img class="video-cover" data-original="https://v-huya-img2.msstatic.com/1908/124326929/1.jpg" alt="拉风龙：全队的希望 13杀吃鸡">





def check():
    name = 'lucy'
    messagebox.showinfo('结果', name)

top = tkinter.Tk()
# 窗口标题
top.title('lucy_test')
# 窗口大小
top.geometry('400x300')
# 文本
label = tkinter.Label(top, text='Hello World')
label.pack()
# 按钮
quit_button = tkinter.Button(top, text='关闭', command=top.quit)
quit_button.pack()
do_button = tkinter.Button(top, text='打印', command=check)
do_button.pack()
# 显示窗口
tkinter.mainloop()





