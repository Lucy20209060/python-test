arr = [1,2,3,4,5,6,7,8,9,10,11]

#  [a:b] 截取你a-b位 不包括b位
print(arr[1:3])
print(arr[0:4])

# 截取到第三位
print(arr[:3])
# 倒数第三位
print(arr[-3])
# 从倒数第5位截取到倒数第一位
print(arr[-5:-1])
# 从倒数第五位开始截取到最后一位
print(arr[-5:])

# 相当于复制
print(arr[:])

# 步长 不能为 0 
# 第二位开始 两步拿一位数字
print(arr[1:8:2]) # [2, 4, 6, 8] 
# 第一位开始 两步拿一位数字
print(arr[0:8:2]) # [1, 3, 5, 7]

# 步长为负数时 从有到左提取数字
# arr[8:3:-1] # [9,8,7,6,5]

# 序列相加
print([1,2,3]+[4,5,6]) # [1,2,3,4,5,6]

# len 数组长度
print(len(arr))
# max 数组最大值
print(max(arr))
# min 数组最小值
print(min(arr))

# del 删除第三位元素
del arr[2]

# 末尾添加
arr.append(11)
print(arr)

# count 统计某元素出现次数
print(arr.count(11))

# extend 合并两个数组
a = [1,2,3]
b = [3,4,5]
# 将b数组合并到数组
a.extend(b)
print(a)

# index 返回某个值的索引位置
print(a.index(2))

# insert 插入
# 索引1的位置插入0
a.insert(1,0)
print(a)

# pop 删除元素 默认删除最后一个 并返回删除的元素
c = [8,7,6,5,4]
c.pop()
print(c)
# 删除索引3位置的元素
c.pop(3)
print(c)

# remove 移除匹配的第一个元素
d = [1,2,3,4,53,2,3,3]
# 移除了第一个 3
d.remove(3)
print(d)

# reverse 倒序 不返回值
d.reverse()
print(d)

# sort 排序
e = [1,2,3,4,53,2,3,3]
# 不返回列表副本
e.sort()
print(e)

# sorted 返回列表副本
f = sorted(e)
print(f)
