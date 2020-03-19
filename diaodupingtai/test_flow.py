import datetime
import time
import unittest
from time import sleep
from selenium import webdriver
from diaodupingtai.test_Integrated_monitoring import Integrated_monitoring, playback
from diaodupingtai.test_basic_configuration import personnel_equipment, data_setting, user, basic_configuration, fenqu
from diaodupingtai.test_intelligent_scheduling import intelligent_scheduling, scheduling_settings, information_service, tools
from diaodupingtai.test_operation_chart import operation_chart
from diaodupingtai.test_statistical_analysis import statistical_analysis, data
from diaodupingtai.test_system_maintain import system_maintain


#李晓龙
from diaodupingtai.text_add_thirdstage.basic_configuration_priceinformation import priceinformation, teamset, material, reason ,Alarm,information ,DeviceList,carparameter,drivermessage,groupmanagement,User,truckyieldalter
from diaodupingtai.text_add_thirdstage.basic_configuration_priceinformation import Logindriverenquiry,truckrunning,truckpresent,excavatoroperation,excavatorpresent,unloadoperation,unloadpresent
from diaodupingtai.text_add_thirdstage.basic_configuration_priceinformation import standbycar,readycar,delayedcar,faultcar,leavecar,readyaffirm,broken_SHOVEL002,unloadmine_SHOVEL002,broken_SHOVEL001,unloadmine_SHOVEL001,excavator_SHOVEL002,excavator_SHOVEL001
from diaodupingtai.text_add_thirdstage.basic_configuration_priceinformation import siteset,lockprohibited,basicinformation





class test_tage(unittest.TestCase):

    # def save_img(self, img_name):  # 错误截图方法，这个必须先定义好
    #     """
    #         传入一个img_name, 并存储到默认的文件路径下
    #         :param img_name:
    #         :return:
    #     """
    #
    #     browser.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(r"D:\Test_Project\img"), img_name))

    @classmethod
    def setUpClass(cls):
        global browser
        browser = webdriver.Chrome()  # 实例化Chrome类
        time.sleep(2)  # 使程序暂停2秒，下同
        # 浏览器最大化
        browser.maximize_window()
        # 隐式等待
        browser.implicitly_wait(30)
        global login_pagesource
        login_pagesource = browser.page_source

    # 关闭浏览器
    @classmethod
    def tearDownClass(cls):
        print("完成退出")
        browser.quit()

    # 登录测试

    def test_login(self):
        '''登录测试'''
        browser.get("http://42.159.80.130:9999/")
        time.sleep(2)
        browser.find_element_by_name("username").send_keys("itage@i-tage.com")
        time.sleep(2)
        browser.find_element_by_name("password").send_keys("i-tage")
        time.sleep(2)
        #browser.find_element_by_xpath('//*[@id="app"]/div/section/main/div/div/div[1]/div/form/div[4]/button').click()
        browser.find_element_by_xpath('//*[@id="app"]/div/section/main/div/div/div[1]/div/form/div[5]/button').click()
        time.sleep(2)
        content = u"首页"
        self.assertEqual(content,browser.title)

    # 信息管理（基础配置测试）
    # @BeautifulReport.add_test_img('test_basic_configuration')  # 失败后会有报错截图
    def test_basic_configuration(self):
        '''1.1信息管理-基础配置'''
        basic_configuration(browser)
        test1 = try_assert("分区管理")
        self.assertEqual(test1, 1)

#李晓龙_基于“基础设置”第三级目录开发---------------------
    def Test_information(self):
        '''1.1.1分区信息'''
        information(browser)
        test1_information = try_assert(u"分区信息")
        self.assertEqual(test1_information, 1)
        time.sleep(3)

    def Test_priceinformation(self):
        '''1.1.2台阶信息'''
        priceinformation(browser)
        test1_priceinformation = try_assert(u"台阶信息")
        self.assertEqual(test1_priceinformation, 1)
        time.sleep(3)

    def Test_teamset(self):
        '''1.1.3班组设置'''
        teamset(browser)
        test2_priceinformation = try_assert(u"班组设置")
        self.assertEqual(test2_priceinformation, 1)
        time.sleep(3)

    def Test_material(self):
        '''1.1.4物料类别'''
        material(browser)
        text3_priceinformation = try_assert(u"物料类别")
        self.assertEqual(text3_priceinformation, 1)
        time.sleep(3)

    def Test_reason(self):
        '''1.1.5原因类型'''
        reason(browser)
        text4_priceinformation = try_assert(u"原因类型")
        self.assertEqual(text4_priceinformation, 1)
        time.sleep(3)

    def Test_Alarm(self):
        '''1.1.6报警配置'''
        Alarm(browser)
        text5_priceinformation = try_assert(u"报警配置")
        self.assertEqual(text5_priceinformation, 1)
        time.sleep(3)



# 李晓龙_基于“人员设备”第三级目录开发---------------------
        # fenqu(browser)
        # test2 = try_assert("人员设备")

    def Test_personnel_equipment(self):
        '''1.2信息管理-人员设备'''
        personnel_equipment(browser)
        test1 = try_assert("人员设备")
        self.assertEqual(test1, 1)
        sleep(3)

    def Test_DeviceList(self):
        '''1.2.1设备列表'''
        DeviceList(browser)
        test2 = try_assert("设备列表")
        self.assertEqual(test2, 1)
        sleep(3)

    def Test_carparameter(self):
        '''1.2.2车辆参数'''
        carparameter(browser)
        test3 = try_assert("车型参数")
        self.assertEqual(test3, 1)
        sleep(3)

    def Test_drivermessage(self):
        '''1.2.3司机信息'''
        drivermessage(browser)
        test4 = try_assert("司机信息")
        self.assertEqual(test4, 1)
        sleep(3)


# 李晓龙_基于“用户管理”第三级目录开发---------------------
    def Test_user(self):
        '''1.3信息管理-用户管理'''
        user(browser)
        test1 = try_assert("用户管理")
        self.assertEqual(test1, 1)
        sleep(3)

    def Test_groupmanagement(self):
        '''1.3.1组管理'''
        groupmanagement(browser)
        test2 = try_assert("组管理")
        self.assertEqual(test2, 1)
        sleep(3)

    def Test_User(self):
        '''1.3.2用户管理'''
        User(browser)
        test3 = try_assert("电子邮箱")
        self.assertEqual(test3,1)
        sleep(3)



# 李晓龙_基于“用户管理”第三级目录开发---------------------
    def Test_datamanage(self):
        '''1.4信息管理-数据管理'''
        data_setting(browser)
        test1 = try_assert("数据管理")
        self.assertEqual(test1, 1)
        # self.save_img('登录')
        sleep(3)

    def Test_truckyieldalter(self):
        '''1.4.1卡车产量修改'''
        truckyieldalter(browser)
        test2 = try_assert("卡车产量修改")
        self.assertEqual(test2, 1)
        sleep(3)

    def Test_Logindriverenquiry(self):
        '''1.4.2登录司机查询'''
        Logindriverenquiry(browser)
        test3 = try_assert("登录司机查询")
        self.assertEqual(test3, 1)
        sleep(3)

    def Test_truckrunning(self):
        '''1.4.3卡车运行状态'''
        truckrunning(browser)
        test4 = try_assert("卡车运行状态")
        self.assertEqual(test4, 1)
        sleep(3)

    def Test_truckpresent(self):
        '''1.4.4卡车当前状态'''
        truckpresent(browser)
        test5 = try_assert("卡车当前状态")
        self.assertEqual(test5, 1)
        sleep(3)

    def Test_excavatoroperation(self):
        '''1.4.5电铲运行状态'''
        excavatoroperation(browser)
        test6 = try_assert("电铲运行状态")
        self.assertEqual(test6, 1)
        sleep(3)

    def Test_excavatorpresent(self):
        '''1.4.6电铲当前状态'''
        excavatorpresent(browser)
        test7 = try_assert("电铲当前状态")
        self.assertEqual(test7, 1)
        sleep(3)

    def Test_unloadoperation(self):
        '''1.4.7卸点运行状态'''
        unloadoperation(browser)
        test8 = try_assert("卸点运行状态")
        self.assertEqual(test8, 1)
        sleep(3)

    def Test_unloadpresent(self):
        '''1.4.8卸点当前状态'''
        unloadpresent(browser)
        test9 = try_assert("卸点当前状态")
        self.assertEqual(test9, 1)
        sleep(3)

# 李晓龙_基于“用户管理”第三级目录开发---------------------
    # 2.1智能调度-调度中心
    def test_intelligent_scheduling(self):
        '''2.1智能调度-调度中心'''
        intelligent_scheduling(browser)
        test1 = try_assert("调度中心")
        self.assertEqual(test1,1)
        sleep(3)

    def Test_standbycar(self):
        '''2.1.1备用卡车'''
        standbycar(browser)
        test2 = try_assert("备用卡车")
        self.assertEqual(test2,1)
        sleep(3)

    def Test_readycar(self):
        '''2.1.2就绪卡车'''
        readycar(browser)
        test3 = try_assert("就绪卡车")
        self.assertEqual(test3, 1)
        sleep(3)

    def Test_delayedcar(self):
        '''2.1.3延时卡车'''
        delayedcar(browser)
        test4 = try_assert("延时卡车")
        self.assertEqual(test4, 1)
        sleep(3)

    def Test_faultcar(self):
        '''2.1.4故障卡车'''
        faultcar(browser)
        test5 = try_assert("故障卡车")
        self.assertEqual(test5, 1)
        sleep(3)

    def Test_leavecar(self):
        '''2.1.5离线卡车'''
        leavecar(browser)
        test6 = try_assert("离线卡车")
        self.assertEqual(test6, 1)
        sleep(3)

    def Test_readyaffirm(self):
        '''2.1.6就绪确认（叹号）'''
        readyaffirm(browser)
        test7 = try_assert("报警信息")
        self.assertEqual(test7, 1)
        sleep(3)

    def Test_broken_SHOVEL002(self):
        '''2.1.7破碎站（SHOVEL002）'''
        broken_SHOVEL002(browser)
        test8 = try_assert("破碎站")
        self.assertEqual(test8, 1)
        sleep(3)

    def Test_unloadmine_SHOVEL002(self):
        '''2.1.8卸点南矿（SHOVEL002）'''
        unloadmine_SHOVEL002(browser)
        test9 = try_assert("卸点南矿")
        self.assertEqual(test9, 1)
        sleep(3)

    def Test_broken_SHOVEL001(self):
        '''2.1.9破碎站（SHOVEL001）'''
        broken_SHOVEL001(browser)
        test10 = try_assert("破碎站")
        self.assertEqual(test10, 1)
        sleep(3)

    def Test_unloadmine_SHOVEL001(self):
        '''2.1.10卸点南矿（SHOVEL001）'''
        unloadmine_SHOVEL001(browser)
        test11 = try_assert("卸点南矿")
        self.assertEqual(test11, 1)
        sleep(3)

    def Test_excavator_SHOVEL002(self):
        '''2.1.11电铲（SHOVEL002）'''
        excavator_SHOVEL002(browser)
        test11 = try_assert("SHOVEL002")
        self.assertEqual(test11, 1)
        sleep(3)

    def Test_excavator_SHOVEL001(self):
        '''2.1.12电铲（SHOVEL001）'''
        excavator_SHOVEL001(browser)
        test11 = try_assert("SHOVEL001")
        self.assertEqual(test11, 1)
        sleep(3)

    #智能调度-调度设置
    def Test_dispatchset(self):
        '''2.2智能调度-调度设置'''
        scheduling_settings(browser)
        test1 = try_assert("调度设置")
        self.assertEqual(test1, 1)
        sleep(3)

    def Test_siteset(self):
        '''2.2.1现场设置'''
        siteset(browser)
        test2 = try_assert("状态设置")
        self.assertEqual(test2, 1)
        sleep(3)

    def Test_lockprohibited(self):
        '''2.2.2锁定禁止'''
        lockprohibited(browser)
        test3 = try_assert("电铲限制")
        self.assertEqual(test3, 1)
        sleep(3)

    def Test_basicinformation(self):
        '''2.2.3基础信息'''
        basicinformation(browser)
        test4 = try_assert("司机修改")
        self.assertEqual(test4, 1)
        sleep(3)











        information_service(browser)
        test3 = try_assert("信息查询")
        sleep(3)
        tools(browser)
        test4 = try_assert("工具箱")
        sleep(3)
        test = test3 & test4
        self.assertEqual(test, 1)

    # 集成监视测试
    def test_Integrated_monitoring(self):
        '''集成监视测试'''
        Integrated_monitoring(browser)
        sleep(3)
        test1 = try_assert("监控中心")
        sleep(5)
        playback(browser)
        sleep(3)
        test2 = try_assert("数据回放")
        sleep(3)
        test = test1 & test2
        self.assertEqual(test, 1)

    # 运行图表测试
    def test_operation_chart(self):
        '''运行图表测试'''
        operation_chart(browser)
        test1 = try_assert("运行图表")
        sleep(3)
        test = test1
        self.assertEqual(test, 1)

    # 统计分析测试
    def test_statistical_analysis(self):
        '''统计分析测试'''
        statistical_analysis(browser)
        test1 = try_assert("统计分析")
        sleep(3)
        data(browser)
        test2 = try_assert("数据中心")
        sleep(3)
        test = test1 & test2
        self.assertEqual(test, 1)

    # 系统维护测试
    def test_system_maintain(self):
        '''系统维护测试'''
        system_maintain(browser)
        self.assertEqual(try_assert("系统维护"), 1)
        sleep(3)


# 字符串包含断言
def try_assert(content):
    login_pagesource = browser.page_source
    try:
        assert content in login_pagesource  # 使用assert断言页面title含某字符
    except AssertionError:  # 若页面不含某字符（即登录失败），则引发AssertionError
        loginerr = "D:\Error\Erro" + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ".png"
        browser.save_screenshot(loginerr)  # 使用save_screenshot方法截图并以LoginErro保存
        return 0
    else:
        return 1