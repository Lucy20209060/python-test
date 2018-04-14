#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

_author_ = 'lucy'

# 导入模块
import sys 
def test():
    args = sys.argv
    if len(args)==1:
        print('hello world')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()


# 第1行和第2行是标准注释
# 第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行
# 第2行注释表示.py文件本身使用标准UTF-8编码
