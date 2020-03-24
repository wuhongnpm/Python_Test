#If语句
a = '1234567890'
b = int(input('输入年份'))
if (a[b % 12]) == '7':
    print('Number is 7')
else:
    print("Number is not 7")
#for语句
for aa in a:
    print(aa)
#遍历1-12
for i in range(1,13):
    print(i)
#while语句
num = 5
while True:
    num = num +1
    if num == 10:
        continue
    print(num)
    tiem.sleep(1)
