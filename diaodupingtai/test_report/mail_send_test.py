#!python3
#codin=utf-8
import yagmail      #yagmail发送邮件使用模块。需要pip安装
import os


from diaodupingtai.test_report.compress import Compress




'''
代码说明：
1\下边的password密码，是你用的QQ邮箱（授权码）输入的。授权码获取方式用百度搜索
2\目前附件发送只接收rar后缀附件
'''

#发送报告
def send_mail():
    '''
    代码说明：
    1\下边的password密码，是你用的QQ邮箱（授权码）输入的。授权码获取方式用百度搜索
    2\目前附件发送只接收rar后缀附件
    '''
    yag = yagmail.SMTP(user='734206208@qq.com', password='duqohkvrwfylbfcc', host='smtp.qq.com', port='465')
    body = "以下是《自动驾驶平台》测试报告附件，请查收..."

    Compress()# 启动压缩脚本

    url = report_screen()   #启动 获取报告名称方法
    url_1 = ".\\" + url    #拼接，必须字符串格式  （如果这行不写，下行写一定要，（1，必须引号。2，目录加文件名称） " .\测试报告2020-03-18 11_15_41_.html.zip"  ）

    yag.send(to=['1026994525@qq.com','xiaolong.li@i-tage.com'], subject='《自动驾驶平台》自动化测试报告', contents=[body, url_1])
    print("已发送邮件")


#找出报告
def report_screen():
    url = "D:\\Tage_work\\diaodupingtai\\"  #路径文件夹
    report_name = os.listdir(url)    #展示文件夹下的所有文件名字
    for i in report_name:       #遍历
        zip_1 = os.path.splitext(i)[-1]    #获取每个文件后缀（字符串可用splitext的功能，能获取索引1 就是文件名字的第二索引.   -1是最后一个索引）
        if  zip_1 == ".zip":    #判断获取出的值，是不是   .zip    带小点。会比较
            return i



