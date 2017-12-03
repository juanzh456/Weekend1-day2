import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
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

#7.添加商品描述
driver.find_element_by_name("brief").send_keys("苹果手机很好用，最新款")

#如果定位不到“商品图册”，可以使用javascript滚动滚动条
#driver.execute_script("windows.scrollTo(200,100)")
#7. 添加商品图册
driver.find_element_by_link_text("商品图册").click()
#有些页面控件是javascript在页面加载之后生成的，implicitly_wait是用来判断整个页面是否加载完毕
#有时页面加载完，但是javascript的控件还没有创建完，所以需要加time.sleep(),提高程序的稳定性；
time.sleep(2)
#driver.find_element_by_class_name("webuploader-pick").click() #无法定位到
#driver.find_element_by_css_selector("#filePicker label").click()
#因为真正负责上传文件的页面元素是<input type="file"...>
#所以我们可以直接操作这个控件，直接输入图片的路径
driver.find_element_by_name("file").send_keys("D:/Juan/uploadpicture.png")
#driver.find_element_by_name("file").send_keys("D:/uploadpicture.png")
#点击开始上传，同时用三个class定位，
driver.find_element_by_css_selector(".uploadBtn.state-finish.state-ready").click()
#driver.find_element_by_class_name("button_search").click()
#alert控件不是直接弹出来的，需要时间等待
time.sleep(3)
driver.switch_to.alert.accept()

#页面太长，点击不了下面的button，如何操作滚动条
#range是区间，默认从0开始，到长度-1，range（10）表示0到9，10个数字
ac=ActionChains(driver)
for i in range(10):
    #print("hello word")
    ac.send_keys(Keys.ARROW_RIGHT)
ac.perform()

# 7. 提交
driver.find_element_by_class_name("button_search").click()




