#!/usr/bin/env python  
""" 
@author:Administrator 
@file: zlzhaopin.py 
@time: 2017/12/23 
"""  
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from tools.config import *


class ZhiLianZhaoPin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(base_url)
        self.driver.implicitly_wait(10)
        pass

    def tearDown(self):
        self.driver.quit()
        pass

    def test_zhilian_zhaopin(self):
        driver = self.driver
        driver.find_element_by_id("loginname").clear()
        driver.find_element_by_id("loginname").send_keys(username)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)
        #if driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[2]/form/div[3]/a[1]").is_selected():
        driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[2]/form/div[3]/a[1]").click() #取消勾选"自动登录"
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[2]/form/div[3]/button").click() #点击登录
        driver.implicitly_wait(10)
        self.assertIn("退出",driver.page_source)
        driver.find_element_by_xpath("//*[@id=\"popup_header\"]/span").click()
        #driver.find_element_by_class_name("fr popup_close").click()
        time.sleep(2)
        driver.find_element_by_link_text("职位搜索").click()
        driver.implicitly_wait(10)
        d1 = driver.find_element_by_id("KeyWord_kw2")
        d1.send_keys("软件自动化测试")
        time.sleep(2)
        d1.send_keys(Keys.BACK_SPACE*7)
        time.sleep(2)
        d1.send_keys("自动化软件测试")
        time.sleep(2)
        driver.find_element_by_class_name("doesSearch").click()#点击搜工作
        driver.implicitly_wait(10)

        # driver.find_element_by_xpath("//*[@id=\"newlist_list_content_table\"]/table[2]/tbody/tr[1]/td[1]/input").click()
        # driver.find_element_by_xpath("//*[@id=\"newlist_list_content_table\"]/table[3]/tbody/tr[1]/td[1]/input")
        #driver.find_element_by_xpath("//*[@id=\"newlist_list_content_table\"]/table[61]/tbody/tr[1]/td[1]/input")
        def table_num():
            list1 = list(range(2, 61, 2))
            # list1=[2,4,6,8,10,12,14,16,18]
            for number in list1:
                driver.find_element_by_xpath(
                    "//*[@id=\"newlist_list_content_table\"]/table[{0}]/tbody/tr[1]/td[1]/input".format(
                        int(number))).click()
                #print(number)
        table_num()
        driver.save_screenshot("image.png")
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()
