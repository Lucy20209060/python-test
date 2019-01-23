#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql

def connect():
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
    cursor.execute("select id,code,name from menu;")
    result = cursor.fetchall()
    
    res = []
    for item in result:
        keys = ['id', 'code', 'name']
        res.append(dict(zip(keys, item)))
    
    db.commit()
    db.close()
    
    return res