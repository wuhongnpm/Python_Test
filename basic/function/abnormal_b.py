yc_b = [1, 2, 3]
try:
    for i in [1, 4]:
        print(i)
except IndexError as e:
    print(e)
except SyntaxError as se:
    print(se)
else:
    print("只有再try语句里面的执行成功的时候，才会执行else里面的内容")
