s"""
将华氏温度转换为摄氏温度
"""
f = float(input('请输入华式温度:'))
c = (f -32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f ,c))

"""
输入年份 如果是闰年输出True 否则输出False
"""
year = int(input('请输入年份:'))
is_leap = (year % 4 == 0 and year % 100 != 0 ) or year % 400 ==0
print(is_leap)


"""
用户身份验证
"""

username = input ('请输入用户名: ')
password = input ('请输入密码')
if username == 'admin' and password =='123456':
    print('身份验证成功!')
    else :
        print('身份证失败!')

""""
如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；70分-80分（不含80分）
输出C；60分-70分（不含70分）输出D；60分以下输出E。
"""
score = float(input('请输入成绩:'))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >=70:
    grade = 'C'
elif score >=60:
     grade = 'D'
else:
    grade = 'E'
print('对应的等级是:', grade)