from selenium import webdriver

driver=webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
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
driver.find_element_by_name("username").send_keys("zhangjuan2")
driver.find_element_by_name("mobile_phone").send_keys("18610372136")
driver.find_element_by_css_selector("input[value='1']").click()
#driver.find_element_by_xpath("//input[@value='1']").click()
driver.find_element_by_name("birthday").send_keys("2011-10-12")
driver.find_element_by_name("email").send_keys("1415791787@qq.com")
driver.find_element_by_name("qq").send_keys("1715791756")
driver.find_element_by_class_name("button_search").click()

driver.switch_to.default_content()