#1.准备csv文件，
#2.导入csv包，csv是python语言内置的包
import csv
#3. 知道文件的存储路径，读取数据文件
#字符串前面加一个字符r，表示反斜杠是普通字符，不看做转义字符
path=r"D:\Juan\selenium_python\learning\my_file\Weekend1-day2\data\member_info.csv"
#4. 通过路径打开文件,；
file=open(path,'r')
#5.通过csv代码库，读取csv格式的内容
data_table=csv.reader(file)
#6.遍历data_table，分别打印每一行数据
for row in data_table:
    print(row)



