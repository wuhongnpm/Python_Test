 1 # coding=utf-8
 2 #1.先设置编码，utf-8可支持中英文，如上，一般放在第一行
 3
 4 #2.注释：包括记录创建时间，创建人，项目名称。
 5 '''
 6 Created on 2019-4-23
 7 @author: 北京-宏哥
 8 Project:学习和使用unittest框架编写测试用例执行顺序
 9 '''
10 #3.导入unittest模块
11 import unittest
12 #4.执行顺序和运行测试
13 import unittest
14
15 class TestLogin(unittest.TestCase):
16
17     def test_login_blog(self):
18         """登录博客园
19 
20         :return:
21         """
22
23     def test_add_essay(self):
24         """ 添加随笔
25 
26         :return:
27         """
28
29     def test_release_essay(self):
30         """ 发布随笔
31 
32         :return:
33         """
34
35     def test_quit_blog(self):
36         """退出博客园
37 
38         :return:
39         """
40 if __name__ == "__main__()":
41     unittest.main()