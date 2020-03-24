demo = [x*x for x in range(10)]
print("列表生成式",demo)
d1 = (x*x for x in range(5))
print("生成器",d1)
try:
    print("生成器迭代值",next(d1))
except StopIteration as e:
    print("生成器所有的值已经迭代结束")
