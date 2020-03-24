#导入 unittest 这个模块
import unittest

#class 这一行是定义一个测试的类，并继承 unittest.TestCase 这个类
class IntegerArithmeticTestCase(unittest.TestCase):
   # 接下来是定义了两个测试case名称: testAdd和testMultiply4、注释里面有句话很重要：
   #test method names begin 'test*'--翻译：测试用例的名称要以 test 开头
    def testAdd(self):  # test method names begin with 'test'
        result = 10-5
        hope = 5
        self.assertEqual(result, hope)

##然后是断言 assert，这里的断言方法是 assertEqual-判断两个是否相等，这个断言可以是一个也可以是多个
    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)

#if 下面的这个 unittest.main()是运行主函数，运行后会看到测试结果
if __name__ == '__main__':
    unittest.main()