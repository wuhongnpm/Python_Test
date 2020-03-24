ditc1 = {}
print(type(ditc1))
#字典定义
dict2 = {'a':1,'b':2}
#字典增加
dict2['c'] = 3
print(dict2)

#计算1到10的平方
alist = []
for i in range(1,11):
    if (i % 2 == 0):
        alist.append(i*i)
print(alist)

#计算1到10的平方
#列表推导式
blist = [i*i for i in range(1,11) if (i % 2) ==0]
print(blist)

#字典推导式
略