##os.path模块

import os
import sys
import datetime

#返回目录
print("返回当前执行文件的目录: %s" % os.path.dirname(__file__))
print(os.path.dirname("返回当前文件的工作空间目录: %s" % os.path.dirname(__file__)))

#返回当前工作目录
print("返回当前工作目录: %s" % print(os.getcwd()))

#判断路径是否存在
pwd1 = os.path.dirname(__file__)
pwd2 = "OperateFile"
print("如果路径存在,返回True: %s" % os.path.exists(pwd1))
print("如果路径存在,返回False: %s" % os.path.exists(pwd2))

#返回一个绝对路径
print("返回一个绝对路径: %s,注意它的盘符是当前操作系统的默认盘符" % os.path.abspath(pwd1))

#返回路径的最后一部分
print("返回路径的最后一部分: %s" % os.path.basename(pwd1))

#返回文件名
print("返回文件名 %s" % os.path.basename(__file__))

#将路径切割成头和尾的一个元组
print("将路径切割成头和尾的一个元组: (%s,%s)" % os.path.split(pwd1))

#拼接一个路径
#print("拼接一个路径: %s " % os.path.join("D:xx",r"joinFile"))


print("%s" % sys.platform)
print("%s" % os.name)




