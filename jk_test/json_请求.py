import requests
import  json


url ="https://www.kuaidi100.com/query?type=zhongtong&postid=73124853607476&temp=0.9490992175423745&phone=  "
headers = {
     "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
 } # get 方法加个 User-Agent 就可以了
s = requests.session()
r = s.get(url, headers=headers,verify=False)
result = r.json()

#以上是代码模拟接口请求

data = result['data'] # 获取 data 里面内容
print (data)
print (data[0]) # 获取 data 里最上面有个
get_result = data[0]['context'] # 获取已签收状态
print (get_result)
#以上取到接口返回结果
#下面是进行断言
if u"已签收" in get_result:
  print ("快递单已签收成功")
else:
  print ("未签收")