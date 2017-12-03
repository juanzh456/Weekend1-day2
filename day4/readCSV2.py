#1.之前的readCSV不能被其他测试用例调用，所以应该给这段代码封装到一个方法里
import csv
#2. 每个测试用例的路径不同，所以path应该作为参数传入到这个方法中
#3.我们打开了一个文件，但如果没有关闭，最终会造成内存泄露
import os


def read(file_name):
    #所有的重复代码的出现，都是程序设计的不合理
    #重复的代码应该封装到一个方法里
    current_file_path = os.path.dirname(__file__)
    path = current_file_path.replace("day4","data/"+file_name)
    #因为file文件一旦被关闭，里面的数据也随着消失
    #所以单独声明一个列表result，来保存里面的数据（不使用数据是因为数据长度固定）
    result=[]
    #file=open(path,'r') #打开数据文件，并只读
    # with语句是一个代码块，代码块里的语句应该缩进4个空格
    #with代码块可以自动关闭with中声明的变量file
    with open(path, 'r') as file:
        data_table=csv.reader(file)
        for row in data_table:
            result.append(row)
            #print(row)
    return result
    #如果在打开和关闭程序的代码中间发生了异常，导致后面的代码不能运行
    #导致file.close()也不执行，这时文件仍然不能关闭，应该用with...as...实现
    #file.close()

if __name__ == '__main__':
    # 这是个绝对路径，实际工作中，一个项目不止一个人编写代码
    #我们没法统一要求大家把项目代码放在一个路径下，并且也会因为项目路径文件路径而不同
    #所以应该在代码中，通过当前代码文件的路径，根据相对路径，找到csv文件
    #所以首先要找到当前文件的路径
    #os 设操作系统，path是路径，dir是directory目录，__file__是python内置变量，指当前文件

    #current_file_path=os.path.dirname(__file__)
    #print(current_file_path)
    # path = r"D:\Juan\selenium_python\learning\my_file\Weekend1-day2\data\member_info.csv"
    # read(path)
    # 获取csv数据文件路径
    # path=current_file_path.replace("day4",r"data/member_info.csv")
    # print(path)
    member_info=read("member_info.csv")
    #print(member_info)
    #5.
    for row in member_info:
        #print(row) #打印每一条数据
        print(row[0]) #打印每一条数据的第一列