# 返回智能调度
import time

def intelligent_scheduling(browser):
    # print("打开智能调度")
    browser.find_element_by_xpath("//div[@class='header-nav-list']").click()
    time.sleep(3)
    # browser.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/section[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/a[1]/div[1]").click()
    browser.find_element_by_xpath("//div/section/header/div/div/div[1]/div/div[2]/div[3]/a/div/div[1]/span[1]").click()


#点击调度设置
def scheduling_settings(browser):
    # print("打开调度设置")
    browser.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/section[1]/header[1]/div[1]/div[1]/ul[1]/li[2]/div[1]/a[1]/div[1]/span[1]").click()
    time.sleep(3)

#点击信息查询
def information_service(browser):
    # print("打开信息查询")
    browser.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/section[1]/header[1]/div[1]/div[1]/ul[1]/li[3]/div[1]/a[1]/div[1]/span[1]").click()
    time.sleep(3)


#点击工具箱
def tools(browser):
    # print("打开工具箱")
    browser.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/section[1]/header[1]/div[1]/div[1]/ul[1]/li[4]/div[1]/a[1]/div[1]/span[1]").click()
    time.sleep(3)