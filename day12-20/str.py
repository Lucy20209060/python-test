#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 头部注释 防止编码错误 导致报错

str = 'hello world!!'
# 字符串截取
# 1-7 截取1-7位 不包括第七位
tem = str[1:7]
print(tem)

# 截取到第七位 不包括第七位
tem2 = str[:7]
print(tem2)

# 倒数第3位
print(str[-3])

# 转义 \
# print('Let\'s go')
# print("\"Hello world\"")

# 输出用户输入的内容
# name1 = input("Enter your name?")
# print(name1)

# 绝对值
# print(abs(-2))
# 2

# 转换为浮点数
# print(float(4))
# 4.0

# find 找到包含的字符串的位置 返回其位置 没有则返回 -1
# find('o',5) 提供开始位置 和 结束位置
a = 'Hello world Fuck you'
print(a.find('wo')) # 6

# join 连接为字符串
b = ['1','2','3','4','5']
print('+'.join(b))			# 1+2+3+4+5

# lower 转化为小写

c = 'that\'s all folks'
# 首字母大写 冠词也会被大写
print(c.title()) 		# That'S All Folks

# 正确将首字母大写了
import string
d = string.capwords(c)
print(d)				# That's All Folks

# replace 返回替换后的字符串
# 将 'all'替换为'a'
e = c.replace('all','a')
print(e)					# that's a folks

# splict 将字符串分割为序列 与join相反
f = '1+2+3+4+5+6+7'
print(f.split('+'))