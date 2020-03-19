import time

# 返回统计分析
def statistical_analysis(browser):
    # print("打开统计分析")
    browser.find_element_by_xpath("//div[@class='header-nav-list']").click()
    time.sleep(3)
    browser.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/section[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[6]/a[1]/div[1]").click()

#点击数据中心
def data(browser):
    # print("打开数据中心")
    browser.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/section[1]/header[1]/div[1]/div[1]/ul[1]/li[2]/div[1]/a[1]/div[1]/span[1]").click()
    time.sleep(3)