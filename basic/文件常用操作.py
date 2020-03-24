#文件常用操作
#进行逐行处理
file1 =  open('name.txt')
for line in file1.readlines():
    print(line)
    print('=====')

file2 = open('name.txt')
print(file2.tell()) #告诉用户文件指针在哪
file2.read(1) #指针到1,下一行时打印输出
print(file2.tell())
file2.seek(0) #seek()方法指定相对位置
print(file2.tell())
#seek()方法的第一个参数保湿偏移位置,第二个参数表示 0表示从文件开头偏移 1表示从当其位置偏移 2从文件结尾
file2.seek(5,0)
print(file2.tell())