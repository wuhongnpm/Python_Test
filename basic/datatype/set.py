set0 = {"A",'a','a',"B"}
set1 = set({"C","D",'e',(12,2)})
set2 = frozenset({"G","F","不变集合"})

#增(add,update)
set0.add("加一")
print(set0)
set0.update("t")
print(set0)

#删除pop remove discard
set0.pop()
print(set0)
set0.remove('A')
print(set0)
set0.discard('W')#未找到则无视
print(set0)

set4 = {"1","2"}
set5 = {"3","4"}
#关系运算,交集,并集,差集,issubset,isupperset
print("交集&",set4 & set5)
print("差集",set4 - set5)
print("并集",set4 | set5)
print("交叉布集",set4 ^ set5)
print("issubset前是否时后的子集", set4.issubset(set5))
print("isupperset前是否是后的父集",set4.issubset(set5))
