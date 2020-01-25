# -*- coding: utf-8 -*-
"""
@Time : 2019/12/4 13:55
@Author : Spider fu
@File : change_chrome_ip.py
模拟浏览器，动态切换ip
"""
import MySQLdb.cursors
from scrapy.selector import Selector
from selenium import webdriver
options = webdriver.ChromeOptions()
conn1 = MySQLdb.connect('127.0.0.1', 'root', 'fuzizhu', 'education_db', charset="utf8", use_unicode=True)
cur1 = conn1.cursor()
cur1.execute("SELECT ip,port FROM `proxy_ip` ")
result1 = cur1.fetchall()
print(result1)
for proxy in result1:
    ip = proxy[0]
    port = proxy[1]
    print(ip,port,"更换的ip")
    options.add_argument('--proxy-server=http://'+str(ip)+':'+str(port)+'')
    driver = webdriver.Chrome(executable_path="D:/chromedriver/chromedriver_win32/chromedriver.exe", chrome_options=options)
    try:
        driver.get("http://httpbin.org/ip")
        j_selector = Selector(text=driver.page_source)
        result = j_selector.css("body > pre::text").extract()[0]
        print(result)
    except Exception as a:
        driver.quit()