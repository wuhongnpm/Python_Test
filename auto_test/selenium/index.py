from selenium import  webdriver

browser = webdriver.Chrome(executable_path="../../../../../zc/chromedrive/chromedriver.exe")
browser.get('https://testerhome.com/')


size=browser.set_window_size(800,600)
browser.get_screenshot_as_file("D:\\a.png")