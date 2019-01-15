#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 类
class Dog:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def sayName(self):
		print('my name is ' + self.name + ', I am ' + str(self.age) + ' years old')


mydog = Dog('lucy',20)
mydog.sayName()
print(mydog.name)