#索引,切片
list_demo1 = [123,'string',[1,2,3],(1,2,3),{"App":"1"},True]
index_list = list_demo1[2]
print(index_list)
section_list= list_demo1[0:3]
print(section_list)

#追加append,整体添加
list42 = list_demo1
list42.append([1,2])
print(list42)

#扩展extend,分解添加
list43 = list_demo1
list43.extend([1,4])
print(list43)

#插入insert
list44 = list_demo1
list44.insert(3,"O")
print(list44)

#取出pop
list45 = list_demo1
list45.pop()
print(list45)

#删除remove,del
list46 = list_demo1
list46.remove("string")
print(list46)
del list46[0]
print(list46)

#排序
list47 = [23,5,3,222,344]
print(sorted(list47))
print(sorted(list47,reverse=True))


