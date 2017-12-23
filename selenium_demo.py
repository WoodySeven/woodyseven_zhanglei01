#!/usr/bin/env python  
""" 
@author:Administrator 
@file: selenium_demo.py 
@time: 2017/12/23 
"""  
import selenium
import time
from selenium import webdriver


browser = webdriver.Chrome()
print(browser.name)
browser.get("http://cn.bing.com")
print(browser.title)
browser.find_element_by_id("sb_form_q").send_keys("samren 博客园")
print(browser.current_url)
browser.find_element_by_id("sb_form_go").click()
# print(browser.page_source)
time.sleep(2)
browser.quit()