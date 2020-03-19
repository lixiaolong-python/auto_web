import time

# 返回运行图表
def operation_chart(browser):
    # print("打开运行图表")
    browser.find_element_by_xpath("//div[@class='header-nav-list']").click()
    time.sleep(3)
    browser.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/section[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[5]/a[1]/div[1]").click()