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
from selenium.webdriver.support.select import Select


class DanShuangSelect(unittest.TestCase):
    """鼠标悬浮"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        self.driver.get("http://test1.zmninfo.com/SimulationElement/")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    # def test_xia_la_kuang(self):
    #     driver=self.driver
    #     select1=driver.find_element_by_name("s1")
    #     Select(select1).select_by_value("o2")
    #     time.sleep(2)

    # def test_dan_xuan_kuang(self):
    #     driver = self.driver
    #     select2 = driver.find_element_by_name("r1")
    #     select2.click()
    #     time.sleep(2)

    def test_fu_xuan_kuang(self):
        driver = self.driver
        select3 = driver.find_element_by_xpath("/html/body/form[4]/table/tbody/descendant::input[last()]")
        select3.click()
        time.sleep(1)
        select3.click()
        time.sleep(1)
        select4 = driver.find_elements_by_name("c1")
        for i in select4:
            i.click()
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()
