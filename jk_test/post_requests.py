#发送post请求的接口（dict参数）
import  requests

url = 'http:bin.org/bin'
payload = {"username":'3210682950@qq.com',"passowrd":'mcaddd'}#值以字典的形式传入
response = requests.post(url=url,data=payload)
print(response.text)


#或是发送post请求的接口（json参数）
#post 的 body 是 json 类型，也可以用 json 参数传入。2、先导入 json 模块，用 dumps 方法转化成 json 格式。3、返回结果，传到 data 里
import  requests
import json
url = 'https://www.baidy.com'
payload = {"username":'213123123',"password":'231312213'}#值以字典形式传入
data_json = json.dumps(payload) #转换成json格式
response = requests.post(url=url,json=data_json)
print(response.text)

#现在的网站安全性很高,一般上面的都不行.举一个header的例子
import  requests
import  json
url = 'http:bin.org/bin'
headers = {
    "Connection": 'xxx',"Host":"xx.org","User-Agent":"xx"
}
response = requests.post(url=url,headers=headers,verify=False)
print(response.text)
print(response.json())
