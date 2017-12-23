#!/usr/bin/env python  
""" 
@author:Administrator 
@file: bugfree_login_unittest.py 
@time: 2017/12/23 
"""
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select


class BugFreeLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://192.168.2.87/bugfree"
        self.driver.get(self.base_url)
        pass

    def tearDown(self):
        self.driver.quit()
        pass

    def test_bug_free_login(self):
        self.driver.find_element_by_id("LoginForm_username").clear()
        self.driver.find_element_by_id("LoginForm_username").send_keys("admin")
        self.driver.find_element_by_id("LoginForm_password").send_keys("123456")
        Select(self.driver.find_element_by_id("LoginForm_language")).select_by_value("en")
        self.driver.find_element_by_id("SubmitLoginBTN").click()
        time.sleep(3)
        self.assertIn("list", self.driver.current_url)
        self.assertIn("退出", self.driver.page_source)


if __name__ == "__main__":
    unittest.main()
