#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql

#
# 数据库连接与断开
#
def sql_operation(fun):
    def foo():
        global cursor
        config = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'passwd': '12345678',
            'db': 'python_test',
            'charset': 'utf8'
        }
        db = pymysql.connect(**config)
        cursor = db.cursor()
        result =  fun()
        db.commit()
        db.close()
        return result
    return foo


#
# menu菜单
#
@sql_operation
def menu_list():
    cursor.execute("select id,code,name from menu;")
    result = cursor.fetchall()
    res = []
    for item in result:
        keys = ['id', 'code', 'name']
        res.append(dict(zip(keys, item)))
    return res