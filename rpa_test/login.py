#!/usr/bin/python
# -*- coding: utf-8 -*-
import execjs
import requests
import json
import io

session = requests.session()
acounts = 'luchao'
password = '123456'

def get_js():
    f = io.open("../js/RSA.js", 'r', encoding='UTF-8')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr

def password_encry(password):
    global session
    pas = password[::-1]
    req = session.get('http://rpa.aliyun.net/rpa/user/sso/rsa/public/hex')
    data = req.json()['data']
    jsstr = get_js()
    ctx = execjs.compile(jsstr)
    return (ctx.call('returnPas', data['publicExp'], '', data['publicKey'], pas))

password =  password_encry(password)

# 登录
login_data = {
    'userName': acounts,
    'password': password
}
login = session.post('http://rpa.aliyun.net/rpa/user/sso/login/hex', data=login_data)
if login.json()['success'] == True:
    print('/rpa/user/sso/login/hex -> 登录成功')
else:
    print('/rpa/user/sso/login/hex -> ' + login.json()['msg'])

# 个人信息
baseinfo = session.get('http://rpa.aliyun.net/rpa/user/baseinfo')
if baseinfo.json()['success'] == True:
    print('/rpa/user/baseinfo -> 成功返回个人信息')
else:
    print('/rpa/user/baseinfo -> ' + baseinfo.json()['msg'])

# 菜单列表
menu_list = session.get('http://rpa.aliyun.net/rpa/auth/page/menu/list')
if menu_list.json()['success'] == True:
    print('/rpa/auth/page/menu/list -> 成功返回菜单列表')
else:
    print('/rpa/auth/page/menu/list -> ' + menu_list.json()['msg'])


# 无人值守型机器人列表
robot_unattended_data = {
    'name': '', # 机器人昵称
    'clientTypeCd': 'robot_unattended', # 无人
    'currentPage': 1,
    'pageSize': 20
}
client_list = session.get('http://rpa.aliyun.net/rpa/client/list',data=robot_unattended_data)
if client_list.json()['success'] == True:
    print('/rpa/client/list -> 成功返回无人值守型机器人列表第'+str(robot_unattended_data['currentPage'])+'页')
else:
    print('/rpa/client/list -> ' + client_list.json()['msg'])