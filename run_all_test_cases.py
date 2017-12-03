import unittest


if __name__ == '__main__':
    #defaultTestLoader默认的测试用例加载器,用于寻找符合一定规则的测试用例
    #discover发现
    suite=unittest.defaultTestLoader.discover('./day5',pattern='*Test.py')
    #执行suite中的所有的测试用例
    #TextTestRunner文本的测试用例运行器, 首字母大写,说明它是个类,添加()即可实例化对象,不需要new关键字
    unittest.TextTestRunner().run(suite)
