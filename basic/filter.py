# def counter():
#     cnt = [0]
#     def add_one():
#         cnt[0] +=1
#         return cnt[0]
#     return  add_one
# num1 = counter()
#
# print(num1())
# import  time
#
# def timmer(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         stop_time = time.time()
#         print("运行时间是 %秒" % (stop_time - start_time))
#     return  wrapper
#
# @timmer
# def i_can_sleep():
#     time.sleep(3)


fd = open('name.txt')
try:
    for line in fd:
        print(line)
finally:

 with open('name.txt') as f:
    for line in f:
        print(line)

