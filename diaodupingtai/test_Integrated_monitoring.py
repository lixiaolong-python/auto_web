import time

# 返回集成监视
def Integrated_monitoring(browser):
    # print("打开集成监视")
    browser.find_element_by_xpath("//div[@class='header-nav-list']").click()
    time.sleep(3)
    browser.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/section[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/a[1]/div[1]").click()

# 点击数据回放
def playback(browser):
    # print("打开数据回放")
    browser.find_element_by_xpath(
        "/html[1]/body[1]/div[1]/div[1]/section[1]/header[1]/div[1]/div[1]/ul[1]/li[2]/div[1]/a[1]/div[1]/span[1]").click()
    time.sleep(3)