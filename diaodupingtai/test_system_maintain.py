import time

# 返回系统维护
def system_maintain(browser):
    # print("打开系统维护")
    browser.find_element_by_xpath("//div[@class='header-nav-list']").click()
    time.sleep(3)
    browser.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/section[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[7]/a[1]/div[1]").click()
    time.sleep(3)