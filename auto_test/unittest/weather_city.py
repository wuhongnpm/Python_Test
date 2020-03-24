import requests
import unittest
#4.编写测试用例和断言
class TestWeather(unittest.TestCase):
    '''测试天气预报接口'''       # 此注释将展示到测试报告的测试组类
    def test_beijin_weather(self):
         '''查询北京天气预报'''         # 此注释将展示到测试报告的用例标题
         url = "https://www.apiopen.top/weatherApi"

         par = {
                 "city": "北京",  # 城市名
         }
         r = requests.post(url, params=par)
         print(r.text)     # 获取返回的结果
         result = r.json()['code'] #获取状态码
         print(result)
         # 断言
         self.assertEqual(200, result)
         self.assertIn('msg', r.text)
         self.assertTrue('北京'in r.text)
    def test_nanjin_weather(self):
         '''查询南京天气预报'''  # 此注释将展示到测试报告的用例标题
         url = "https://www.apiopen.top/weatherApi"
         par = {
             "city": "南京",  # 城市名
           }
         r = requests.post(url, params=par)
         print(r.text)  # 获取返回的结果
         result = r.json()['code']#获取状态码
         print(result)
         # 断言
         self.assertEqual(200, result)
         self.assertIn('msg', r.text)
         self.assertTrue('南京' in r.text)

 if __name__ == "__main__":
     unittest.main()