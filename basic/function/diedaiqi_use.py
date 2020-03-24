from collections.abc import Iterable, Iterator
list1 =range(5)
for i in list1:
    print(i)
#将可迭代对象转换为迭代器对象
if isinstance(list1,Iterable):
    print("该对象是可迭代对象")
elif isinstance(list1,Iterator):
    print("该对象是迭代器")
else:
    print("您的判断不存在")

list2 = iter(list1)
try:
    print("迭代器对象获取数据:",next(list2))
except StopIteration as e:
    print("That is all floks!")

