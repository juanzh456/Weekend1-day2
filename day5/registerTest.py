#有了myTestCase以后,再写测试用例 就不需要重新写setUp和tearDown方法
import os

from selenium import webdriver

from day5.myTestCase import MyTestCase


class Register(MyTestCase):
    #3个双引号表示文档字符串,也是一种注释,和#号的区别是这种注释会显示在文档中
    """注册模块测试用例"""
    #因为myTestCase 依据实现了setUp和tearDown方法,以后再写测试用例就不需要重新实现折两个方法了

    def test_register(self):
        """打开注册页面的测试用例"""
        driver=self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.current_url #用来获取当前浏览器的网址
        actual=driver.title #用来获取当前浏览器标签的title
        expected="用户注册 - 道e坊商城 - Powered by Haidao"
        base_path=os.path.dirname(__file__)
        path=base_path.replace('day5','report/image/')
        #get_screenshot_as_file()截取当前浏览器图片
        driver.get_screenshot_as_file(path+"regist.png")
        #如果报错浏览器版本错误,需要重新安装或下载新的driver
        self.assertEqual(actual,expected)
        print("成功打开测试页面")