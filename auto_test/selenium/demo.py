from selenium import webdriver
browser = webdriver.Chrome(executable_path="../../../../../zc/chromedrive/chromedriver.exe")
browser.get('http://www.baidu.com/')

#在搜索框输入极客时间
browser.find_element_by_name("wd").send_keys("极客时间")
browser.find_element_by_name("wd").submit()


