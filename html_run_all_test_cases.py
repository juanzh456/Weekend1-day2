import os
import smtplib
import unittest
#HTMLTestRunner是基于unittest框架的一个扩展,可以自己在网上下载
import time
from email.header import Header
from email.mime.text import MIMEText

from lib.HTMLTestRunner import HTMLTestRunner


def send_mail(path):
    f=open(path,'rb')
    mail_body=f.read() #读取html报告的内容,作为邮件的正文
    f.close()

    #要想发邮件,我们要把二进制的内容转成MIME格式
    #MIME multipurse多用途 Internet互联网 Mail邮件 Extension 扩展
    #这种格式是对邮件协议的一个扩展,使邮件不仅支持文本格式,还支持多种格式,比如图片,音频,二进制文件等
    msg=MIMEText(mail_body,'html','utf-8')
    #上面是邮件的正文,但是对于一个邮件来讲,除了正文,还需要主题,发件人,收件人
    #msg是字典的类型,字典类似于数组,区别是:1. 字典是无序的,
    msg['Subject']=Header("自动化测试报告",'utf-8')
    #如果想用客户端软件或者自己写代码登陆邮箱,很多类型的邮件,需要单独设置一个客户端授权码,为了安全着想
    msg['From']='bwftest126@126.com'
    msg['To']='zhongguo241@163.com'

    #邮件内容已经准备好了,下面开始发送邮件
    #发邮件的手动步骤:
    #1.打开登陆页面,即连接邮箱服务器
    #要想连接服务器,首先必须搞清楚网络传输协议,http, https,ftp,socket
    #126邮箱支持pop3,smtp,imap
    #首先导入smtplib的代码库,
    smtp=smtplib.SMTP()  #实例化一个SMTP类的对象
    smtp.connect("smtp.126.com")  #链接126邮箱
    #2.登陆邮箱
    smtp.login('bwftest126@126.com','abc123asd654')
    #3.发送邮件
    #注: msg是string类型,
    smtp.sendmail("bwftest126@126.com", "zhongguo241@163.com", msg.as_string())
    #4.退出邮箱
    smtp.quit()
    print("Email has sent out!")


if __name__ == '__main__':
    #时间戳
    #str是String,f是format格式,
    #strftime()通过这个方法可以定义时间格式
    #Y year, m month, d day, H hour, M minute, S second
    now=time.strftime("%Y-%m-%d_%H-%M-%S")


    suite=unittest.defaultTestLoader.discover('./day5','*Test.py')
    #unittest.TextTestRunner() 文本测试用例运行器
    #现在用html的测试用例运行器
    #html的测试用例运行器最终会生成一个html的测试报告
    #我们要指定测试报告的路径
    base_path=os.path.dirname(__file__ )
    path=base_path+"/report/report"+now+".html"
    file=open(path,'wb')
    #file.close()
    HTMLTestRunner(stream=file,title="海盗商城测试报告",
                   description="测试环境:window server 2008 + Chrome").run(suite)
    #这时生成的测试报告,只显示类名和方法名,只能给专业的人士查看
    #我们应该将相关的手动测试用例的标题加到我们的测试报告
    #我们自动化测试用例是从手工测试用例中挑出来的,所以我们的代码里应该体现手工测试用例的标题
    #在测试类和方法里添加"""注释"""

    #新的测试报告会覆盖原来的测试报告,如果想要把原来的测试报告保存起来
    #则加一个时间戳,按照当前时间计算一个数字,把数字作为文件名的一部分,避免文件被重写

    #现在我们的html格式的测试报告生成了,当测试用例全部执行完成,
    #我们应该生成一份邮件提醒,通知所有关系测试结果的认
    #我们要把html报告作为邮件正文,发邮件
    file.close()
    send_mail(path)


