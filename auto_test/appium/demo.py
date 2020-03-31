
from appium import webdriver

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "m3"
caps["appPackage"] = "com.douban.frodo"
caps["appActivity"] = "com.douban.frodo.MainActivity"
caps["autoGrantPermissions"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.widget.ImageView")
el1.click()
el2 = driver.find_element_by_id("com.douban.frodo:id/search_hint")
el2.click()
el3 = driver.find_element_by_id("com.douban.frodo:id/search")
el3.send_keys("0")
el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout")
el4.click()
el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView")
el5.click()

driver.quit()