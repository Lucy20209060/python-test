#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from time import sleep

# hosts 需要加上 127.0.0.1	localhost
# 否则启动后没有反应

browser = webdriver.Chrome()
browser.get("http://rpa.aliyun.net/login")
# 帐号登录
browser.find_element_by_id("userName").clear()
browser.find_element_by_id('userName').send_keys('luchao')
# 密码输入
browser.find_element_by_id("passwordName").clear()
browser.find_element_by_id('passwordName').send_keys('123456')
# 点击登录
browser.find_element_by_xpath('//*[@id="ice_container"]/div/div/div/div[2]/div/div[2]/button[1]').click()
sleep(5)
browser.close()