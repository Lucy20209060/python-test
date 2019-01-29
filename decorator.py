#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 目标函数带固定参数
# def decorator(fun):
#     def wrapper(*args, **kwargs):
#         print(args, kwargs)
#         print '妈妈来了'
#         fun(*args, **kwargs)
#         print '开始叠被子'
#     return wrapper

# def decorator(parent):
#     def _decorator(fun):
#         def wrapper(*args, **kwargs):
#             print(args, kwargs)
#             print parent + '来了'
#             fun(*args, **kwargs)
#             print '开始叠被子'
#         return wrapper
#     return _decorator
    
# @decorator
# def foo(name):
#     print name + '起床了'

# @decorator
# def bar(name1, name2):
#     print name1 + '和' + name2 + '起床了'

# @decorator('爸爸')
# def baz(name):
#     print name + '起床了'

# # foo('Lucy')
# baz('Lucy')
# print(baz.__name__)

class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print('class decorator runing')
        self._func()
        print('class decorator ending')


@Foo
def bar():
    print('bar')

bar()