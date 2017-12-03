import unittest

import time
from selenium import webdriver


class LoginTest(unittest.TestCase):
    """登录模块测试用例"""
    def setUp(self):
        #打开浏览器
        #driver=self.driver;
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        #浏览器的版本和driver的版本必须匹配才能用窗口最大化
        self.driver.maximize_window()

    def tearDown(self):
        #driver=self.driver;
        time.sleep(10)
        self.driver.quit()

    def test_login(self):
        """登录测试正常情况测试用例"""
        driver=self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element_by_name("username").send_keys("zj123")
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_class_name("login_btn").click()
        print("登录成功")

if __name__ == '__main__':
    unittest.main()