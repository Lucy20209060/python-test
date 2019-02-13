#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd # 读
import xlwt # 写

# 打开表格
excel = xlrd.open_workbook(r'/Users/lc/Desktop/test.xls')
# 获取表格所有工作表名称
# print (excel.sheet_names())

# 获取工作表的三种方式
table = excel.sheets()[1]
# table = excel.sheet_by_name('table2')
# table = excel.sheet_by_index(1)

# 获取工作表有效行
# print (table.nrows)

# 检查某个工作表是否导入完毕
# table1 = excel.sheet_loaded(1)
# print(table1)

# 获取某行的数据 返回由该行中所有的单元格对象组成的列表
rowx = table.row(1)
print(rowx)

# for item in table.get_rows():
#     print(item)

# table = data.sheets()[0]          #通过索引顺序获取

# table = data.sheet_by_index(sheet_indx) #通过索引顺序获取

# table = data.sheet_by_name(sheet_name)#通过名称获取