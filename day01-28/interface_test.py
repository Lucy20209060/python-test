#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from time import sleep
import requests
import json

def get_chrome_cookie(accounts, password):
    browser = webdriver.Chrome()
    browser.get("http://rpa.aliyun.net/login")
    # 帐号登录
    browser.find_element_by_id("userName").clear()
    browser.find_element_by_id('userName').send_keys(accounts)
    # 密码输入
    browser.find_element_by_id("passwordName").clear()
    browser.find_element_by_id('passwordName').send_keys(password)
    # 点击登录
    browser.find_element_by_xpath('//*[@id="ice_container"]/div/div/div/div[2]/div/div[2]/button[1]').click()
    c = browser.get_cookies()
    chrome_cookie =  c[0]['name'] + '=' + c[0]['value']
    # req = requests.get('http://rpa.aliyun.net/rpa/user/login/Token')
    # print(req.json())
    browser.close()
    return {
        'Cookie': chrome_cookie
    }

# 获取cookie
chrome_cookie = get_chrome_cookie('luchao', '123456')

req1 = requests.get('http://rpa.aliyun.net/rpa/user/baseinfo', cookies=chrome_cookie)
print(req1.json()['data'])
print(req1.headers)

req2 = requests.get('http://rpa.aliyun.net/rpa/message/unread/count', headers=chrome_cookie)
print(req2.json())
