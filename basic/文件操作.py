#对文件进行基本的读写操作,以下是内置函数
#open()打开文件
#read()输入
#readline()输入一行
#seek()文件内移动
#write()输出
#close()关闭文件

#将小说的人物记录在文件中
#open('name.txt')默认只读方式写入
file1 = open('name.txt','w')
file1.write('诸葛亮')
file1.close()

#读取文件
file2 = open('name.txt')
print(file2 .read())
file2.close()

#写入文件
file3 = open('name.txt','a')
file3.write('刘备')