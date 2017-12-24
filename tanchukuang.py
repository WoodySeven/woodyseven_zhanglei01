#!/usr/bin/env python  
""" 
@author:Administrator 
@file: mouse_actionchains.py
@time: 2017/12/24
"""
import unittest
import selenium
import time
from selenium import webdriver
from selenium.webdriver import ActionChains


class TanChuKuang(unittest.TestCase):
    """弹出框"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        self.driver.get("http://test1.zmninfo.com/SimulationElement/")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_mouse_action_chains(self):
        driver=self.driver
        driver.find_element_by_name("b1").click()
        alert1 = driver.switch_to.alert  #选择进弹出框
        time.sleep(1)
        print(alert1.text)  #可以打印出弹出框文本
        alert1.accept()#确认选择
        #alert.dismiss()#取消选择
        time.sleep(1)

        driver.find_element_by_name("b2").click()
        alert2 = driver.switch_to.alert  # 选择进弹出框
        time.sleep(1)
        print(alert2.text)  # 可以打印出弹出框文本
        alert2.send_keys("随便输入信息")
        time.sleep(1)
        alert2.accept()
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()
