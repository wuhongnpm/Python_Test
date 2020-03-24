from collections.abc import Iterable, Iterator

ddq = "ABCDSEF"
list1 = range(10)
if isinstance(ddq,Iterable):
    print("该对象是可迭代对象")
elif isinstance(ddq,Iterator):
    print("该对象时迭代器")
else:
    print("判断不存在")