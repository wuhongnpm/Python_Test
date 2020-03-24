#PyTest模板用例
#引入***
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestDemo:
    def setup(self): #driver初始化
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "bluestack"
        caps["appPackage"] = "com.google.android.youtube"
        caps["appActivity"] = "com.google.android.apps.youtube.app.WatchWhileActivity"
        caps["autoGrantPermissions"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(1)#添加隐式等待

    def test_demo(self):        #用例部分
        el1 = self.driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"Subscriptions\"]/android.widget.ImageView")
        el1.click()
        el2 = self.driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"Library\"]/android.widget.ImageView")
        el2.click()
        el3 = self.driver.find_element_by_accessibility_id("Search")
        el3.click()
        el4 = self.driver.find_element_by_id("com.google.android.youtube:id/search_edit_text")
        el4.click()
        el4.send_keys("wuhong-CCC")

    #添加设备交互
    def test_gsm_call(self):
        self.driver.send_sms("123131233","Hello,Form Linyi")
        #self.driver.make_gsm_call("12321312",GsmCallActions.CALL)

    def test_performance(self):
        print(self.driver.get_performance_data_types())
        for p in self.driver.get_performance_data_types():
            try:
                print(self.driver.get_performance_data("com.google.android.youtube",p,5))
            except:
                pass
        
    def teartdown(self):
          self.driver.quit()