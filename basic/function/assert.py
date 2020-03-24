assert  1 == 1
try:
    assert 1 == 2
except AssertionError as e:
    print("断言的判断条件为错,异常已捕获: %s " % e)