#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 头部注释 防止编码错误 导致报错

# str = 'hello world!!'
# 字符串截取
# 1-7 截取1-7位 不包括第七位
# tem = str[1:7]
# print(tem)

# 截取到第七位 不包括第七位
# tem2 = str[:7]
# print(tem2)

# 倒数第3位
# print(str[-3])

class Animal:
    def __init__(self, name):
        self.name = name
      
    @classmethod
    def say_hello(clas):  # 类方法，由类调用，最少要有一个参数cls，调用的时候这个参数不用传值，自动将类名赋值给cls
        print(clas)

Animal.say_hello()


class A:
    def __init__(self,name):
        self.name = name
    def sayHello(self):
        print('hello--'+self.name)

a = A('Lucy')


delattr(a,'name')
# delattr(a,'sayHello')
# a.sayHello()

print(dir(list))