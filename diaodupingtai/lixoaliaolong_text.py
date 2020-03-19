from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.maximize_window()

browser.get("http://42.159.80.130:9999/")
time.sleep(2)
browser.find_element_by_name("username").send_keys("itage@i-tage.com")
time.sleep(2)
browser.find_element_by_name("password").send_keys("i-tage")
time.sleep(2)
        #browser.find_element_by_xpath('//*[@id="app"]/div/section/main/div/div/div[1]/div/form/div[4]/button').click()
browser.find_element_by_xpath('//*[@id="app"]/div/section/main/div/div/div[1]/div/form/div[5]/button').click()
time.sleep(3)


browser.find_element_by_xpath("//div[@class='header-nav-list']").click()
time.sleep(2)
browser.find_element_by_xpath("//div/section/header/div/div/div[1]/div/div[2]/div[3]/a/div/div[1]/span").click()

time.sleep(2)
print("打开完毕")
#离线卡车
browser.find_element_by_xpath("//div/div/button[5]").click()

time.sleep(2)

#设置离线卡车(TG1_测试部)
browser.find_element_by_xpath("//div/div/div[10]/p").click()
time.sleep(2)





# 信息设定下↓------------------------------
#发送信息
browser.find_element_by_xpath("//div/div[1]/h4").click()
time.sleep(2)
#当前物料
browser.find_element_by_xpath("//div/div[8]/h4").click()
time.sleep(2)
#输入当前物料，需要输入已有物料名称
browser.find_element_by_name("curntMtrlSn").send_keys("物料")
time.sleep(4)
#点击确认
browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/button[2]").click()
time.sleep(2)


#调度目标
browser.find_element_by_xpath("//div/div[9]/h4").click()
#司机
browser.find_element_by_xpath("//div/div[10]/h4").click()
#锁定
browser.find_element_by_xpath("//div/div[11]/h4").click()
#禁止
browser.find_element_by_xpath("//div/div[12]/h4").click()
#位置
browser.find_element_by_xpath("//div/div[13]/h4").click()
#设备状态
browser.find_element_by_xpath("//div/div[14]/h4").click()
#基本参数
browser.find_element_by_xpath("//div/div[15]/h4").click()


time.sleep(3)

browser.quit()
# time.sleep(3)
# js = "var q=document.body.scrollTop=100"
# browser.execute_script(js)