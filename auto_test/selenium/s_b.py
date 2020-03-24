from selenium import webdriver

browser = webdriver.Chrome(executable_path="..\..\..\zc\chromedrive\chromedriver.exe")
# executable_path来指定chromedirver路径
browser.get ('https://www.douban.com/')
"""
print("登录douban")
browser.find_element_by_class_name("lnk-book").click() print("点击读书")
handles_list = browser.window_handles print(handles_list) browser.switch_to.window(str(handles_list[-1])) print("切换窗⼝口")
if browser.current_window_handle == str(handles_list[-1]): print("切换窗⼝口成功...")
"""
#等待:为了页面加载完成才点击元素,避免找不到元素的现象. 一共有三种等待,硬编码等待,全局隐示等待,显示等待
#使⽤用⽅方式:显示等待 > 全局隐示等待 > 硬编码等待
"""
硬编码等待 time.sleep(1) 不推荐
全局隐式等待:
browser.get("https://www.douban.com") print("登录douban")
browser.implicitly_wait(10) # 会等待每个元素最⼤大时间10s browser.find_element_by_class_name("lnk-book").click() print("点击读书")
显示等待:
WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "lnk-book"))).click() # 显示等待lnk-book 5s
"""
#常用方法
#获取窗口大小页面的高宽高
print browser.get_window_size()
#获取cookies
print(browser.get_cookie())
#设置网络
print(browser.set_network_conditions(
                offline=False,
                latency=5,  # additional latency (ms)
                download_throughput=500 * 1024,  # maximal throughput
                upload_throughput=500 * 1024)  # maximal throughput)
            )
#获取title
print(browser.title)
#获取页面元素
print(browser.page_source)
#获取页面url
print(browser.current_url)
#页面放大
browser.maximize_window()
#页面缩小
browser.minimize_window()
#设置页面大小
browser.set_window_size(300,300)
#向前
browser.forward()
#后退
browser.back()
#滑到底部 js="window.scrollTo(0,document.body.scrollHeight)" browser.execute_script(js)
#滑动到顶部 js="window.scrollTo(0,0)" browser.execute_script(js)

"""
#滑动解锁
#获取拖动条
dragger = browser.find_elements_by_class_name("slide-to-unlock-handle")[0]
#获取拖动条进度条长度
dragger_text = browser.find_elements_by_class_name("slide-to-unlock-bg")[0]
x = dragger_text.location["x"]
action = ActionChains(browser)
 #鼠标左键按下不放
action.click_and_hold(dragger).perform()
#平行移动大于解锁的长度的距离
try:
    action.drag_and_drop_by_offset(dragger,x, 0).perform()
    print("滑动...")
except Exception as e:
    print("faild")
"""
"""
#关闭弹框
time.sleep(10)
try:
    tt = browser.switch_to_alert()
    print("打印警告框提示...")
except Exception as e:
    print("faild")
success_text = tt.text
print(success_text)
tt.accept()
"""
#保存截图
browser.save_screenshot("/Users/xinxi/PycharmProjects/selenium_demo/screen_folder/截图.png")
#图片流截图
"""
sc_str = browser.get_screenshot_as_png()
sc_path = "/Users/xinxi/PycharmProjects/selenium_demo/screen_folder/截图.png"
with open(sc_path,"w") as f:
    f.write(sc_str)
"""

