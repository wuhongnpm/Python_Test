#设计一个common的类，它的父类是object
class Common(object)
    #common的构造函数
    def __int__(self):
        #被测系统的跟路由
     self.url_root = 'http://www.baidu.com'
    #封装get请求吗，url是访问路由，params是get请求的参数，没有默认为空。
    def get(self,url, params=''):
        #拼凑访问地址
      url = self.url_root + url + params
     #通过get请求访问对应地址
      res = requests.get(url)
      #返回requests的response结果
      return res
    #封装自己的post方法，url是访问路由，params是post请求需要传递的参数，如果没有参数这里为空
    def post(self, url params''):
      #拼凑访问地址
      url = self_url_root + url
      if len(params) > 0:
          #如果有参数,那么通过post方式访问对应的url,并将参数赋值给requests.post默认参数data
          #返回request的Response结构,类型为requests的Response类型
          res = requests.post(url)
    return res
