
#捕获异常
try:
    year = int(input('input year:'))
except ValueError:
    print('年份要输入数字')