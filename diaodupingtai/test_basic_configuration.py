import time


def basic_configuration(browser):
    # print("打开基础配置")
    browser.find_element_by_xpath("//div[@class='header-nav-list']").click()
    time.sleep(3)
    browser.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/section[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/a[1]/div[1]").click()

def fenqu():
    pass
# 点击人员设备
def personnel_equipment(browser):
    # print("打开人员设备")
    browser.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/section[1]/header[1]/div[1]/div[1]/ul[1]/li[2]/div[1]/a[1]/div[1]/span[1]").click()
    time.sleep(3)



#点击用户管理
def user(browser):
    # print("打开用户管理")
    browser.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/section[1]/header[1]/div[1]/div[1]/ul[1]/li[3]/div[1]/a[1]/div[1]/span[1]").click()
    time.sleep(3)


#点击数据管理
def data_setting(browser):
    # print("打开数据管理")
    browser.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/section[1]/header[1]/div[1]/div[1]/ul[1]/li[4]/div[1]/a[1]/div[1]/span[1]").click()
    time.sleep(3)
