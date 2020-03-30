def a(x):
    def b(y): return x+y
    return b
#b(y)是闭包