# 导入模块
from selenium import webdriver
 
driver=webdriver.PhantomJS()
url="https://www.baidu.com"
driver.get(url)
# 获取cookie列表
cookie_list=driver.get_cookies()
print(cookie_list)
cookie_dict = {}
# 格式化打印cookie
for cookie in cookie_list:
    cookie_dict[cookie['name']]=cookie['value']
print(cookie_dict)