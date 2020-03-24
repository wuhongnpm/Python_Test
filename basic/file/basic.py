#读文件
import codecs
f_read =codecs.open('qs.txt','rb',encoding="utf-8")
print(f_read.read())
f_read.close()

#写文件
f_write = codecs.open('qs.txt','wb',encoding="utf-8")
f_write.write("ABC")
f_write.close()

#常用方法
#1.readlines():读取所有行,直到结束符EOF并返回列表
f_readlines = codecs.open('qs.txt','rb',encoding="utf-8")
f_a = f_readlines.readlines()
print(type(f_a))
print(f_a)
print(f_a[0])
f_readlines.close()

#2.realine():用于从文件读取整行,包括"\n"字符,如果指定一个非负数,则返回制定大小的字节数,包括'\n"字符.
# __next__():返回迭代器的下一个指向.
f_readline = codecs.open('qs.txt','rb',encoding="utf-8")
f_b= f_readline.readline()
print(f_b)
#print(f_readline.__next__())
f_readline.close()

#writelines():用于向文件中写入一序列的字符串
f_writelines = codecs.open('qs.txt','rb',encoding="utf-8")
#f_c = f_writelines.write("2131nnnn3\n\n")
#f_d = f_writelines.writelines(["123123\n","12333\n"])
f_writelines.close()

#tell()返回当前位置
f_tell = codecs.open('qs.txt','rb',encoding="utf-8")
print(f_tell.tell())

#seek():用于移动文件读取指针到制定位置
f_seek = codecs.open('qs.txt','rb',encoding="utf-8")
f_seek.seek(0)
f_seek.writelines(["222\n"])
f_seek.close()

#name()读取文件名
f_name = codecs.open('qs.txt','rb',encoding="utf-8")
print(f_name.name)

flush(): 刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入。一般情况下，文件关闭后会自动刷新缓冲区，
# 但有时你需要在关闭前刷新它，这时就可以使用 flush() 方法。

#文件操作中经常会忘记文件的关闭操作，使用with操作会避免这一情况的发生。
with codecs.open('qs.txt', 'wb', encoding='utf-8') as f_with:
    f_with.write("test with.")
    print("f_with_closed: ", f_with.closed)
print("f_with_closed: ", f_with.closed)