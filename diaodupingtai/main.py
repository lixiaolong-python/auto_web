import datetime
import os
import unittest
from BeautifulReport import BeautifulReport
from diaodupingtai.test_flow import test_tage


#李晓龙
from diaodupingtai.test_report.mail_send_test import send_mail

root_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
test_dir = root_dir + '/testcases'
report_dir = root_dir + '/test_report/data'


if __name__ == '__main__':
    print('------软件测试自动化：登录界面测试用例------')
    suite = unittest.TestSuite()
    # 将测试用例加入到测试容器(套件)中
    suite.addTest(test_tage("test_login"))
    suite.addTest(test_tage("test_basic_configuration"))
    suite.addTest(test_tage("Test_information"))
    suite.addTest(test_tage("Test_priceinformation"))
    suite.addTest(test_tage("Test_teamset"))
    suite.addTest(test_tage("Test_material"))
    suite.addTest(test_tage("Test_reason"))
    suite.addTest(test_tage("Test_Alarm"))
    suite.addTest(test_tage("Test_personnel_equipment"))
    suite.addTest(test_tage("Test_DeviceList"))
    suite.addTest(test_tage("Test_carparameter"))
    suite.addTest(test_tage("Test_drivermessage"))

    suite.addTest(test_tage("Test_user"))
    suite.addTest(test_tage("Test_groupmanagement"))
    suite.addTest(test_tage("Test_User"))

    suite.addTest(test_tage("Test_datamanage"))
    suite.addTest(test_tage("Test_truckyieldalter"))#卡车产量修改
    suite.addTest(test_tage("Test_Logindriverenquiry"))#登录司机查询
    suite.addTest(test_tage("Test_truckrunning"))#卡车运行状态
    suite.addTest(test_tage("Test_truckpresent"))#卡车当前状态
    suite.addTest(test_tage("Test_excavatoroperation"))#电铲运行状态
    suite.addTest(test_tage("Test_excavatorpresent"))#电铲当前状态
    suite.addTest(test_tage("Test_unloadoperation"))#卸点运行状态
    suite.addTest(test_tage("Test_unloadpresent"))#卸点当前状态


    suite.addTest(test_tage("test_intelligent_scheduling"))
    suite.addTest(test_tage("Test_standbycar"))#备用卡车
    suite.addTest(test_tage("Test_readycar"))# 就绪卡车
    suite.addTest(test_tage("Test_delayedcar"))#延时卡车
    suite.addTest(test_tage("Test_faultcar"))#故障卡车
    suite.addTest(test_tage("Test_leavecar"))#离线卡车
    suite.addTest(test_tage("Test_readyaffirm"))#就绪确认（闪动叹号）
    suite.addTest(test_tage("Test_broken_SHOVEL002"))  #破碎站（SHOVEL002）
    suite.addTest(test_tage("Test_unloadmine_SHOVEL002"))  #卸点南矿（SHOVEL002）
    suite.addTest(test_tage("Test_broken_SHOVEL001"))  #破碎站（SHOVEL001）
    suite.addTest(test_tage("Test_unloadmine_SHOVEL001"))  #卸点南矿（SHOVEL001）
    suite.addTest(test_tage("Test_excavator_SHOVEL002"))  #电铲（SHOVEL002）
    suite.addTest(test_tage("Test_excavator_SHOVEL001"))  #电铲（SHOVEL001）

    #智能调度-调度设置
    suite.addTest(test_tage("Test_dispatchset"))#调度设置
    suite.addTest(test_tage("Test_siteset"))#现场设置
    suite.addTest(test_tage("Test_lockprohibited"))#锁定禁止
    suite.addTest(test_tage("Test_basicinformation"))#基础信息








    suite.addTest(test_tage("test_Integrated_monitoring"))
    suite.addTest(test_tage("test_operation_chart"))
    suite.addTest(test_tage("test_statistical_analysis"))
    suite.addTest(test_tage("test_system_maintain"))
    # 定义个报告存放路径，支持相对路径。
    # filename = "./result.html"
    # fp = open(filename, "wb")
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')
    # # 执行测试用例
    # runner.run(suite)
    run = BeautifulReport(suite) #实例化BeautifulReport模块
    now = datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')
    filename = '测试报告' + str(now)
    run.report(filename=filename,description='踏歌智行线上测试',report_dir=report_dir)

    import time
    # time.sleep(200)
    send_mail()