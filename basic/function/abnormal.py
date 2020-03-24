yc = [1,2,3]

try:
    for i in yc:
        print(yc[i+2])
    raise TypeError("主动抛出异常")
except IndexError as e:
    print("异常 % 已经捕获,下面再有不捕获了" %e)
except Exception as e:
    print(e)
finally:
    print("程序执行结束,不管异常是否被捕获,这里一定执行")