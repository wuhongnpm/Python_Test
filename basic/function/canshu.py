#普通参数
def para_a(para1, para2): #形参
    print(para1)
para_a(100,200) #实参

#默认参数,调用时没有传入的值,用默认,有则用传入.
def para_b (para1,para2,moren="默认值JK"):
    print("moren")
    print(para1)
    print(para2)

para_b("WWW",22)

#动态参数:可以接受任意个参数,有两种args和kwargs,其中args必须在kwargs前面.
#*agr接受按位置传参的值,返回一个元组.**kwargs接受按关键字传参的值,组成一个字典.
def dtcanshu (para1,para2,*args,**kwargs):
    print(para1)
    print(para2)
    print(args)
    print(kwargs)

dtcanshu(1,2,3,4)

