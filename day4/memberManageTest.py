import unittest
import time
from selenium import webdriver

import csv
#1.导入ddt代码库
import ddt

#from day4.readCSV2 import read, reada
#from day4.readCSV2 import reada
from day4.readCSV2 import read

#2.装饰这个类(ddt[文件].ddt[类名])
@ddt.ddt
class MemberManageTest(unittest.TestCase):
    #3.调用之前写好的read（）方法，获取配置围巾中的数据
    member_info=read("member_info.csv")
    #在当前类中只执行一次
    @classmethod
    def setUpClass(cls):
        print("在所有方法之前，执行一次")
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(20)
        cls.driver.quit()

    def test_a_log_in(self):
        print("用户登录")
        driver=self.driver
        driver.get("http://localhost/index.php?&m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("userpass").send_keys("password")
        driver.find_element_by_name("userverify").send_keys("1234")
        driver.find_element_by_class_name("Btn").click()

    #python中集合前面的星号表示把集合中的所有元素拆开，一个一个写
    #list=["小红","小明"]
    #list="小红","小明"
    #加入一个方法需要接收两个参数，那么肯定不能传一个list进去
    #但是如果list中正好也是两个元素，这时在列表前面加一个星号，就不被认为是一个列表，而是两个参数
    #5. ddt.data()测试数据来源于read（）方法
    #把数据表中的每一行传入方法，在方法中增加一个参数row
    @ddt.data(*member_info)
    def test_b_add_member(self,row):
        print("添加会员")
        driver=self.driver
        # 每组测试数据就是一条测试用例，每条测试用例应该是独立的，不能因为上一条测试用例的执行失败，
        # 导致下一组数据不能被正常执行，所以不推荐用for循环
        #应该用ddt装饰器，去修饰这个方法，达到每条测试用例独立执行

        #4.注释掉for循环，改变代码的缩进shift+tab
        #for row in read("member_info.csv"):
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()

        # 添加会员信息
        #如果frame没有name属性时，我们可以通过其他定位方式，
        # iframe_css="#mainFrame"
        # iframe_thml=driver.find_element_by_css_selector(iframe_css)
        # driver.switch_to.frame(iframe_thml)
        driver.switch_to.frame("mainFrame")
        driver.find_element_by_name("username").send_keys(row[0])
        driver.find_element_by_name("mobile_phone").send_keys(row[1])
        #driver.find_element_by_css_selector("input[value='"+row[2]+"']").click()
        driver.find_element_by_css_selector('[value="{0}"]'.format(row[2])).click()
        #driver.find_element_by_xpath("//input[@value="+row[2]+"]").click()
        driver.find_element_by_name("birthday").send_keys(row[3])
        driver.find_element_by_name("email").send_keys(row[4])
        driver.find_element_by_name("qq").send_keys(row[5])
        driver.find_element_by_class_name("button_search").click()



        #之前的代码是能够自动运行，但是还不能自动判断程序运行的是否正确
        #我们自动化代码，不能找人总是看着运行，检查是否执行正确
        #断言类似于if...else...,是用来做判断的,期望结果与实际结果一致则测试通过
        actual=driver.find_element_by_css_selector("#datagrid-row-r1-2-0>td:nth-child(1)>div").text
        expected=row[0]
        ##datagrid-row-r1-2-0 > td:nth-child(1) > div
        # if(actual==expected):
        #     print("测试通过")
        # else:
        #     print("测试失败")

        #断言叫assert,断言是框架提供的，要想调用断言，那么必须加上self.
        #因为测试用例类继承了框架中的TestCase类，也继承了这个类中的断言
        #断言特点：
        #1.断言简洁，
        # 2.断言只关注错误的测试用例，只有断言出错时，才会打印信息
        #3.断言报错时，后面的代码将不会继续执行，好处是前面的步骤失败了，后面的步骤就不需继续尝试了，

        # 切换到父框架
        driver.switch_to.parent_frame()
        # 切换到根节点
        # driver.switch_to.default_content()

        #断言
        self.assertEqual(actual,expected)



#执行当前文件中所有的unittest的测试用例
#执行顺序是按照方法的字母顺序执行的
if __name__ == '__main__':
    unittest.main()


