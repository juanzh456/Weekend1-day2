import unittest

import time
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        #打开浏览器
        #driver=self.driver;
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        #浏览器的版本和driver的版本必须匹配才能用窗口最大化
      #  self.driver.maximize_window()

    def tearDown(self):
        #driver=self.driver;
        time.sleep(10)
        self.driver.quit()