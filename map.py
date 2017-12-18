a = {
	'name':'lucy',
	'age':20,
	'len':170,
	'sex':'man'
}

# len 长度
print(len(a))

# 删除
del a['len']
print(a)

# 检测name是否在a中
print('name' in a)

b = {
	'name':'lucy',
	'age':26
}

# 清除字典中的所有项
b.clear()
print(b)