# #读取人物名称
# f = open('name.txt')
# data = f.read()
# print(data.split('|'))
#
# #读取兵器名称
# f2 = open('weapon.txt')
# i = 1
# for  line in f2.readlines():
#     if i % 2 ==1:
#         print(line.strip('\n'))
#     i +=1
#
# f3 = open('sanguo.txt',encoding='GB18030')
# print(f3.read().replace('\n',''))

#函数是对程序逻辑进行结构化的一种编程方法
#函数的定义: def 函数名(): code  return 需要返回的内容
#函数的调用:函数名称()
def func(filename):
    print(open(filename).read())
    print('test func')

func('name.txt')

#函数的可变参数
def funca (a, b, c):
    print('a= %s' %a)
    print('b= %s' %b)
    print('c= %s' %c)
funca(1,2,c=5)

#取得参数的个数
def howlong(first, *other):
    print( 1+len(other))
howlong(100)

#函数作用域
var1 = 123
def funcb():
    print(var1)
funcb()
print(var1)
#函数的迭代器与生成器
list1 = [1,2,3,4,5]
it = iter(list1)
print(next(it))#next一直迭代到全部读取完,再读取就会报错
print(next(it))

#生成器
for i in range(10,20,2):
    print(i)

def demoab(start,stop,step):
    x = start
    while x<stop:
        yield x
        x +=step
for ia in  demoab(10,20,0.5):
    print(ia)