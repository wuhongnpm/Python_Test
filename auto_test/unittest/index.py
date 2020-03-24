import unittest

def one_equation(a, b):
    # 方程无解
    if a == 0:
        raise ValueError("参数错误，分母不能为0")
    # 返回方程的解
    else:
        return b / a


def two_equation(a, b, c):
    if a == 0:
        raise ValueError("参数错误")
    elif b * b - 4 * a * c < 0:
        raise ValueError("方程在有理数范围内无解")
    elif b * b - 4 * a * c == 0:
        return -b / (2 * a)
    else:
        r1 = (-b + (b * b - 4 * a * c) ** 0.5) / 2 / a
        r2 = (-b - (b * b - 4 * a * c) ** 0.5) / 2 / a
        return r1, r2


class TestMath(unittest.TestCase):
    # 测试一元一次方程的求解
    def test_one_equation(self):
        self.assertEqual(one_equation(2, 5), 2.5)

        self.assertTrue(one_equation(4, -28) == -7)

        with self.assertRaises(ValueError):
            one_equation(0, 7)

    # 测试一元二次方程的求解
    def test_two_equation(self):
        r1, r2 = two_equation(1, -3, 2)
        self.assertCountEqual((r1, r2), (1.0, 2.0), '求解出错')
        r1, r2 = two_equation(2, -7, 6)
        self.assertCountEqual((r1, r2), (1.5, 2.0), '求解出错')
        # 断言只有一个解的情形
        r = two_equation(1, -4, 4)
        self.assertEqual(r, 2.0, '求解出错')
        # 断言当a == 0时的情况，断言引发ValueError
        with self.assertRaises(ValueError):
            two_equation(0, 9, 3)
        # 断言引发ValueError
        with self.assertRaises(ValueError):
            two_equation(4, 2, 3)


if __name__ == '__main__':
    unittest.main()
