import time
# '''1.1信息管理-基础配置'''
#分区信息
def information(browser):
    browser.find_element_by_xpath("//div/section/main/div/div/main/div/div/div/div[1]/div[2]/div[1]/button/div/div[1]").click()
    time.sleep(3)

#台价信息
def priceinformation(browser):
    browser.find_element_by_xpath("//div/section/main/div/div/div/div/ul/div[2]/li/span").click()
    time.sleep(3)

#班组信息
def teamset(browser):
    browser.find_element_by_xpath("//div/section/main/div/div/div/div/ul/div[3]/li/div/span").click()
    time.sleep(2)
    # browser.find_element_by_xpath("//div/section/main/div/div/div/div/ul/div[3]/li/ul/div[1]/li").click()
    # time.sleep(2)
    # browser.find_element_by_xpath("//div/section/main/div/div/div/div/ul/div[3]/li/ul/div[2]/li").click()

#物料类型
def material(browser):
    browser.find_element_by_xpath("//div/section/main/div/div/div/div/ul/div[4]/li/span").click()

#原因类型
def reason(browser):
    browser.find_element_by_xpath("//div/section/main/div/div/div/div/ul/div[5]/li/span").click()

#报警配置
def Alarm(browser):
    browser.find_element_by_xpath("//div/section/main/div/div/div/div/ul/div[6]/li/span").click()



#'''1.2信息管理-人员设备'''
#设备列表
def DeviceList(browser):
    browser.find_element_by_xpath("//div/section/main/div/div/main/div/div/div/div[1]/div[2]/div[1]/button/div/div").click()
    time.sleep(2)

#车辆参数
def carparameter(browser):
    browser.find_element_by_xpath("//div/section/main/div/div/div/div/ul/div[2]/li/span").click()
    time.sleep(2)

#司机信息
def drivermessage(browser):
    browser.find_element_by_xpath("//div/section/main/div/div/div/div/ul/div[3]/li/span").click()
    time.sleep(2)





#'''1.3.1信息管理-用户管理
#组管理
def groupmanagement(browser):
    browser.find_element_by_xpath("//div/section/main/div/div/main/div/div/div/div[1]/div[2]/div[1]/button/div/div").click()
    time.sleep(2)

#用户管理
def User(browser):
    browser.find_element_by_xpath("//div/section/main/div/div/div/div/ul/div[2]/li/span").click()
    time.sleep(2)




# '''1.4.1信息管理-数据管理'''
#卡车产量修改
def truckyieldalter(browser):
    browser.find_element_by_xpath("//div/section/main/div/div/main/div/div/div/div[1]/div[2]/div[1]/button/div/div").click()
    time.sleep(2)
#登录司机查询
def Logindriverenquiry(browser):
    browser.find_element_by_xpath("//div/section/main/div/div/div/div/ul/div[2]/li/span").click()
    time.sleep(2)
#卡车运行状态
def truckrunning(browser):
    browser.find_element_by_xpath("//div/section/main/div/div/div/div/ul/div[3]/li/span").click()
    time.sleep(2)
#卡车当前状态
def truckpresent(browser):
    browser.find_element_by_xpath("//div/section/main/div/div/div/div/ul/div[4]/li/span").click()
    time.sleep(2)
#电铲运行状态
def excavatoroperation(browser):
    browser.find_element_by_xpath("//div/section/main/div/div/div/div/ul/div[5]/li/span").click()
    time.sleep(2)
#电铲当前状态
def excavatorpresent(browser):
    browser.find_element_by_xpath("//div/section/main/div/div/div/div/ul/div[6]/li/span").click()
    time.sleep(2)
#卸点运行状态
def unloadoperation(browser):
    browser.find_element_by_xpath("//div/section/main/div/div/div/div/ul/div[7]/li/span").click()
    time.sleep(2)
#卸点当前状态
def unloadpresent(browser):
    browser.find_element_by_xpath("//div/section/main/div/div/div/div/ul/div[8]/li/span").click()
    time.sleep(2)




#智能调度-调度中心
#备用卡车
def standbycar(browser):
    browser.find_element_by_xpath("//div/section/main/div/div[1]/div[2]/div[1]/div/div/div/div[1]/button[1]/div/div").click()
    time.sleep(2)
# '''2.1.2就绪卡车'''
def readycar(browser):
    browser.find_element_by_xpath("//div/section/main/div/div[1]/div[2]/div[1]/div/div/div/div[1]/button[2]/div/div").click()
    time.sleep(2)
# 延时卡车
def delayedcar(browser):
    browser.find_element_by_xpath("//div/section/main/div/div[1]/div[2]/div[1]/div/div/div/div[1]/button[3]/div/div").click()
    time.sleep(2)
# 故障卡车
def faultcar(browser):
    browser.find_element_by_xpath("//div/section/main/div/div[1]/div[2]/div[1]/div/div/div/div[1]/button[4]/div/div").click()
    time.sleep(2)
# 离线卡车
def leavecar(browser):
    browser.find_element_by_xpath("//div/section/main/div/div[1]/div[2]/div[1]/div/div/div/div[1]/button[5]/div/div").click()
    time.sleep(2)
# 就绪确认（叹号）
def readyaffirm(browser):
    browser.find_element_by_xpath("//div/section/main/div/div[2]/div[1]/button").click()
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div/span/span/i").click()

#破碎站（SHOVEL002）
def broken_SHOVEL002(browser):
    browser.find_element_by_xpath("//div/section/main/div/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/div/div[1]/div[1]/div/p").click()
    time.sleep(1)
    browser.find_element_by_xpath("//div/section/main/div/div[2]/header/div/div/button").click()
    time.sleep(1)

#卸点南矿（SHOVEL002）
def unloadmine_SHOVEL002(browser):
    browser.find_element_by_xpath("//div/section/main/div/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/p").click()
    time.sleep(1)
    browser.find_element_by_xpath("//div/section/main/div/div[2]/header/div/div/button").click()
    time.sleep(1)

#破碎站（SHOVEL001）
def broken_SHOVEL001(browser):
    browser.find_element_by_xpath("//div/section/main/div/div[1]/div[1]/div/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/p").click()
    time.sleep(1)
    browser.find_element_by_xpath("//div/section/main/div/div[2]/header/div/div/button").click()
    time.sleep(1)

#卸点南矿（SHOVEL001）
def unloadmine_SHOVEL001(browser):
    browser.find_element_by_xpath("//div/section/main/div/div[1]/div[1]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/p").click()
    time.sleep(1)
    browser.find_element_by_xpath("//div/section/main/div/div[2]/header/div/div/button").click()
    time.sleep(1)

#电铲（SHOVEL002）
def excavator_SHOVEL002(browser):
    browser.find_element_by_xpath("//div/section/main/div/div[1]/div[1]/div/div/div[2]/div[1]/div[3]/div/div[2]/div/p").click()
    time.sleep(1)
    browser.find_element_by_xpath("//div/section/main/div/div[2]/header/div/div/button").click()
    time.sleep(1)

#电铲（SHOVEL001）
def excavator_SHOVEL001(browser):
    browser.find_element_by_xpath("//div/section/main/div/div[1]/div[1]/div/div/div[2]/div[2]/div[3]/div/div[2]/div/p").click()
    time.sleep(1)
    browser.find_element_by_xpath("//div/section/main/div/div[2]/header/div/div/button").click()
    time.sleep(1)


#智能调度-调度设置
#现场设置
def siteset(browser):
    browser.find_element_by_xpath("//div/section/main/div/div/div/div/ul/div[1]/li/div/span").click()
    time.sleep(1)

#锁定禁止
def lockprohibited(browser):
    browser.find_element_by_xpath("//div/section/main/div/div/div/div/ul/div[2]/li/div/span").click()
    time.sleep(1)

#基础信息
def basicinformation(browser):
    browser.find_element_by_xpath("//div/section/main/div/div/div/div/ul/div[3]/li/div/span").click()
    time.sleep(1)










































