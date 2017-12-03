import unittest

import time
from selenium import webdriver


class MemberManageTest(unittest.TestCase):
    #变量前面加上self.,表明是类的本身的变量
    def setUp(self):
        #打开浏览器
        self.driver=webdriver.Chrome() #driver是全局变量
        #self.driver.implicityly_wait(30)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self):
        #quit()退出真个浏览器
        #close()关闭一个浏览器标签，
        #代码编写和调试时需要在quit()前面加个时间等待，在正式允许的时候去掉时间等待
        time.sleep(20)
        self.driver.quit()

    def test_add_member(self):
        driver=self.driver
        # 登录
        driver.get("http://localhost/index.php?&m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("userpass").send_keys("password")
        driver.find_element_by_name("userverify").send_keys("1234")
        driver.find_element_by_class_name("Btn").click()
        # 2.会员管理 添加会员
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()

        #3. 添加会员信息
        driver.switch_to.frame("mainFrame")
        driver.find_element_by_name("username").send_keys("zhangjuan")
        driver.find_element_by_name("mobile_phone").send_keys("18610372138")
        #driver.find_element_by_css_selector("input[value='1']")
        driver.find_element_by_xpath("//input[@value='1']")
        driver.find_element_by_name("birthday").send_keys("2011-10-12")
        driver.find_element_by_name("email").send_keys("1415791787@qq.com")
        driver.find_element_by_name("qq").send_keys("1715791756")
        driver.find_element_by_class_name("button_search").click()

        driver.switch_to.default_content()

#/html/body/div[2]/div[3]/dl/dd/div/div/dl/form/dd/ul/li[3]/b/label[1]/input
#body > div.content > div.install.mt10 > dl > dd > div > div > dl > form > dd > ul > li:nth-child(3) > b > label:nth-child(1) > input[type="radio"]