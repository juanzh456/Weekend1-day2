#dict是字典的缩写, set是集合的缩写,
#python中元组用小括号表示,列表用中括号表示,字典和集合用大括号表示
#比如,同样描述一个学生信息
stu=("001","小明","男",23)
#元组和数组的区别:
#数组可以修改元素的内容,但是不能增加和删除,数组中的所以元素的类型一样
#元组不能增删改,元素的类型不固定
stu=["002","小明","男",23]
#元组和列表的区别:
#元组是只读,不能修改
#列表是可以增删改查的,列表是最常用数据格式
#find_elements()返回的就是列表

stu={"003","小明","男",23}
#元组和集合的区别
#1. 集合是无序,不能用标(索引)的方式查找元素
#2.集合是不可重复的,重复的元素会自动删除

stu={"id":"004","姓名":"小明","性别":"男","年龄":23}
#字典和集合的区别:
#冒号前面的部分交key,后面的二部分交value
#字典是具有自我描述性的,你看见先的key值,就知道value所代表的意思了
#集合也是无序的,key值不能重复,value值可以重复
#如果我想打印集合中的id的值,
print(stu['id'])

