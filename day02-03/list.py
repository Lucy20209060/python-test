#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from collections import Iterator  #迭代器
from collections import Iterable

# print [x*x for x in range(1, 11) if x > 2]

# print [x*x for x in range(1, 11)]

# print [m + n for m in 'ABC' for n in 'XYZ']

# g = (x * x for x in range(11))

# for x in g:
#     print x

# def foo():
#     print 'step 1'
#     yield 1
#     print 'step 2'
#     yield 2
#     print 'step 3'
#     yield 3

# f = foo()
# print f.next()
# print f.next()

# g = iter([1,2,3])
# print g.next()
# print g.next()
# print g.next()
# print g.next()

# g = (x for x in range(1,11))
# # print g.next()
# l = [1,2,3,4,5]

# print isinstance(g,Iterator)     #判断是不是迭代器
# print isinstance(l,Iterable)

# 创建一个迭代器
# g = enumerate(['a', 'b', 'c', 'd'])
# print g.next()

# s = '1 + 4'
# print eval(s)

# 转化为浮点数
# print float(100)
# print float('100')
# print float('a')

# 格式化输出字符串
# print 'My name is {0}, I am from {1}!'.format('Lucy', 'China')

# l = set([1,2,3,4])
# l[0] = 100
# print l

# 全局变量
# print globals()

# print hasattr(list, 'append')
# print help(list)

# class Foo(object):
#     pass
   
# class Bar(Foo):
#     pass
   
# print issubclass(Bar, Foo)

# print list([1,2,3])

# print(value='a',end='-')
