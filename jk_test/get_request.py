import requests

#设置参数
param = {"q":"西游记"}
#多个参数格式：{"key1": "value1", "key2": "value2", "key3": "value3"}

#请求网站豆瓣首页
r = requests.get("https://www.douban.com/search",params=param)

#打印状态码
print(r.status_code)

#conten 字节方式的响应体，会自动为你解码 gzip 和deflate 压缩
print(r.content)
#headers 以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回 None
print(r.headers)
# Requests 中内置的 JSON 解码器，requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取
#print(r.json())
# 获取 url
print(r.url )
# 编码格式，requests自动检测编码
print(r.encoding)
# 获取 cookie
print(r.cookies)
# 返回原始响应体-- r.text #字符串方式的响应体，会自动根据响应头部的字符编码进行解码
print(r.raw)
# 失败请求(非 200 响应)抛出异常
#print(r.raise_for_status())
#打印文本
print(r.text)
