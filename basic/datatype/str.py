#index() 和 find() 的区别：若索引的字符串或序列不在字符串内，
# index--->返回的是ValueError：subString not found，而find--->返回 -1。

#索引
string_demo1 = "abc"
index_a = string_demo1.index("a",0)
print(index_a)

find_a = string_demo1.find("b",0)
print(find_a)

#切片
string_demo2 = "abcderf"
section = string_demo2[0:1]
print(section)

#长度
string_demo3 = "abcdef"
len = len(string_demo3)
print(len)

#遍历..这个demo have some bug
# string4 = "它那么幼稚"
# for ergodic_str in string4:
#     print("ergodic_str: ", ergodic_str)
# for index in range(len(string4)):
#     print("ergodic_str2: ", string4[index])

#删除
string_demo5 = "abcdef"
del string_demo5

#分隔, partition制定分隔符；split指定分隔符分割几次
string_demo6 = "你的苹果是红色的."
fg = string_demo6.partition("-")
print(fg)

#替换,相关方法replace,strip,lstrip,rstrip
string_demo7 = "7pgpgh123213"
th_a = string_demo7.replace('7',"ff",2)
print(th_a)
th_b = string_demo7.strip() #去掉两边的空格
print(th_b)
th_c = string_demo7.lstrip()#去掉左边的空格
print(th_c)
th_d = string_demo7.rsplit()#去掉右边的空格
print(th_d)

#连接
string_demo8 = "MOMOMO"
jo = '*'.join(string_demo8)
print(jo)
string_demo8a = ['2','1','34']
zh = "->".join(string_demo8a)
print(zh)

#大小写转换
#第一个单词首字母大写：capitalize；全部字母小写：lower；全部字母大写：upper；单词首字母大写：title；大写转小写，小写转大写：swapcase
string_demo9 = "Hello World"
dx_a =string_demo9.capitalize()
print(dx_a)
da_b = string_demo9.lower()
print(da_b)
da_c = string_demo9.upper()
print(da_c)
da_b = string_demo9.title()
print(da_b)
da_e = string_demo9.swapcase()
print(da_e)

#判断字符串的内容
# isalnum字符串是数字或字母的组合；isalpha字符串全部是字母；isdigit字符串数字的组合
string_demo10 = "Mad Man 01"
pdzf_a = string_demo10.isalnum()
print(pdzf_a)
pdzf_b = string_demo10.isalpha()
print(pdzf_b)
pdzf_c = string_demo10.isdigit()
print(pdzf_c)

#判断以什么开头
string_demo11 = "How Do You 网"
pdfz_a = string_demo11.startswith("How")
pdfz_b = string_demo11.endswith("w")
print(pdfz_a)
print(pdfz_b)

#格式化输出
string_demo12 = "你是什么大象{name}"
print(string_demo12.format(name="云南象"))
print(string_demo12.format_map({"name":"红象"}))


#扩展
string13 = "name\tage\tsex\nA\t22\tmale\nB\t23\tfmale"
expandtabs_str = string13.expandtabs()
print("expandtabs_str: \n", expandtabs_str)