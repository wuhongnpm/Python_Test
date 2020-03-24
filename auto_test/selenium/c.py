from selenium import webdriver
browser = webdriver.Chrome(executable_path="../../../../../zc/chromedrive/chromedriver.exe")
browser.get('https://www.douban.com/')

# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains

## 引入 Keys 模块
from selenium.webdriver.common.keys import Keys


browser.set_window_size(480,800)
browser.maximize_window()
browser.find_element_by_class_name("bn").click()
browser.back()
browser.forward()

#元素操作
browser.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[1]/form/fieldset/div[1]/input').send_keys('再见珍妮')
browser.find_element_by_class_name("inp-btn").submit()

"""
#鼠标操作
cc = browser.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[2]/ul/li[4]/a')
ActionChains(browser).double_click(cc).perform()
"""

#键盘操作



# print(browser.title)
#browser.quit()
