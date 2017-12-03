from select import select
from selenium import webdriver

#打开浏览器
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(30)
#隐式等待,一经设置
driver.maximize_window()

#打开首页
driver.get("http://localhost/")

#登陆
login_link=driver.find_element_by_link_text("登录")
driver.execute_script("arguments[0].removeAttribute('target')",login_link)
login_link.click()
driver.find_element_by_name("username").send_keys("zj123")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_name("password").submit()

#进入购物商城
driver.find_element_by_link_text("进入商城购物").click()

#搜索
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()
#"body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a > img"
# "body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > p > a"
#iphone_link="div.shop_01-imgbox > a > img"
iphone_link="div.protect_con > div > p > a"
iphone=driver.find_element_by_css_selector(iphone_link)
driver.execute_script("arguments[0].removeAttribute('target')",iphone)
iphone.click()

#加入购物车
driver.find_element_by_id("joinCarButton").click()
driver.find_element_by_class_name("shopCar_T_span3").click()
driver.find_element_by_link_text("结算").click()

#添加新地址
driver.find_element_by_class_name("add-address").click()
driver.find_element_by_name("address[address_name]").send_keys("张娟")
driver.find_element_by_name("address[mobile]").send_keys("18610372130")
#选择下拉框
# driver.find_element_by_css_selector("[value='230000']").click()
# driver.find_element_by_css_selector("[value='231100']").click()
# driver.find_element_by_css_selector("[value='231123']").click()
#下拉框是一种比较特殊的网页元素,selenium专门为下拉框提供了一种定位方式
#需要把这个元素从webdriver类型转换为Select类型,是selenium的类
sheng=driver.find_element_by_id("add-new-area-select")
Select(sheng).select_by_visible_text("黑龙江")
shi=driver.find_elements_by_tag_name("select")[1]
#Select(shi).select_by_index(2)
Select(shi).select_by_value("231100")
#ctrl+左键可以查看源码, 按住ctrl不放然后拖动鼠标到方法可以查看返回值
xian=driver.find_elements_by_tag_name("select")[2]
Select(xian).select_by_index(3)
driver.find_element_by_name("address[address]").send_keys("文化路9号")
driver.find_element_by_name("address[zipcode]").send_keys("120000")
driver.find_element_by_class_name("aui_state_highlight").click()

