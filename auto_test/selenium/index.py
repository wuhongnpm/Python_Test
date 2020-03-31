from selenium import webdriver
dr= webdriver.Chrome(executable_path="../../../../../zc/chromedrive/chromedriver.exe")
# executable_path来指定chromedirver路径
dr.get('https://www.baidu.com')
print(dr.title)
browser.quit()