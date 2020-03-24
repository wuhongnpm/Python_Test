from selenium import webdriver

browser = webdriver.Chrome(executable_path="..\..\..\zc\chromedrive\chromedriver.exe")
# executable_path来指定chromedirver路径
browser.get ('http://www.baidu.com')

""""
chromeOptions 是一个配置 chrome 启动是属性的类。通过这个类，我们可以为chrome配置如下参数（这个部分可以通过selenium源码看到）：
设置 chrome 二进制文件位置 (binary_location)
添加启动参数 (add_argument)
添加扩展应用 (add_extension, add_encoded_extension)
添加实验性质的设置参数 (add_experimental_option)
设置调试器地址 (debugger_address)

"""
#设置不弹出自动化提醒
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('disable-infobars')

#后台运行
option = webdriver.ChromeOptions()
option.add_argument('headless')

#伪装移动装置
options = webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')

"""
#设置开发者模式
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
self.browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)
"""

#禁止加载图片
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)

"""
selenium元素的八种定位方式:
name定位,id定位,class定位, link text定位,xpath定位,css定位, partial link text定位 tag name定位
定位选择顺序:id > class > name > link_text > xpath > css
"""
browser.find_element_by_name("wd").click()
browser.find_element_by_id("su").click()
browser.find_element_by_class_name("mnav").click()
browser.find_element_by_link_text("实时播报").click()
browser.find_element_by_xpath('//*[@id="ptab-3"]/div[2]/div[1]/div[2]/a/div').click()
browser.find_element_by_partial_link_text("地").click()
#browser.find_element_by_css_selector('#result_logo').click()


