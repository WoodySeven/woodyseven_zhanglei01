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


class MouseActionChains(unittest.TestCase):
    """鼠标悬停"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        self.driver.get("http://test1.zmninfo.com/SimulationElement/")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_mouse_action_chains(self):
        driver=self.driver
        move=driver.find_element_by_xpath("/html/body/div[4]/div")
        ActionChains(driver).move_to_element(move).perform()#鼠标悬停
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()
