#测试框架：主要用途是组织和执行测试用例

#1. 导入unittest框架
import unittest

#java中的public的类名和文件名一样
#python中的可以一样，但推荐：文件首字母小写，类名首字母大写，剩下的一样
#2.继承unittest中的父类，然后直接在unittestDemo中编写测试用例
#python中的继承直接用小括号表示
class UnittestMemo(unittest.TestCase):
    #3. 重写父类中的方法setUp
    #def是方法的关键字，setUp是创建
    #类似于手动测试中的预设条件
    def setUp(self):
        print("这个方法将会在测试用例执行前先执行")

    def tearDown(self):
        print("这个方法将会在测试用例方法之后执行")

    #4.编写测试用例方法
    #只有以test开头命名的方法才是测试用例方法，
    #测试用例方法可以直接被运行；普通方法不能直接运行，只有被调用才能运行
    #测试用例方法执行的结果与光标当前位置有关
    def test_log_in(self):  #测试用例方法
        print("登录测试用例执行")
        self.login()

    def login(self):   #普通方法
        print("注册测试用例")

    def test_search(self):
        print("搜索测试用例")

#如果直接执行这个文件，那么就会执行下面的语句
#否则，执行其他文件，import这个文件的时候，下面的代码就不会被执行
if __name__ == '__main__':
    #执行当前文件中所有的unittest的测试用例
    unittest.main()


