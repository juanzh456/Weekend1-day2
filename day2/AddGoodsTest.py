from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
# 1.登陆


driver=webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://localhost/index.php?&m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_class_name("Btn").click()
# 2.商品管理
driver.find_element_by_link_text("商品管理").click()
# 3.添加商品
driver.find_element_by_link_text("添加商品").click()
# 4.商品名称
driver.switch_to.frame("mainFrame")
driver.find_element_by_class_name("text_input").send_keys("iphone X")
#有一种特殊的网页,比如左边或者上边有一个导航条,这时就要查看一个页面是否潜逃多个页面
#其中商品管理和添加商品数以根节点, 商品名称属于frame框架里的子页面
#多个窗口需要切换,frame与主页面之间也需要切换
# 5.选择商品类型
driver.find_element_by_id("1").click()
driver.find_element_by_id("2").click()
driver.find_element_by_id("6").click()
# driver.find_element_by_id("7").click()
# driver.find_element_by_link_text("选择当前分类").click()
#双击是种特殊的元素操作,python被封装到ActionChains这个类中,链表必须以perform方法结尾
#也可以用来执行一组操作,只要最后以perform()结束即可
#java封装到Actions这个类中
ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()
# 6.选择商品品牌
brand=driver.find_element_by_name("brand_id")
Select(brand).select_by_visible_text("苹果 (Apple)")
# 7. 提交
driver.find_element_by_class_name("button_search").click()




