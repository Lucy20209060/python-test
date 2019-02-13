#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlwt # 写
file = xlwt.Workbook()
table = file.add_sheet('工作表1',cell_overwrite_ok=True)
table.write(0,0,'test')
file.save('/Users/lc/Desktop/demo.xls')