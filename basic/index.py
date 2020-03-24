#计算生肖和星座案例
chinese_zodiac = '鼠、牛、虎、兔、龍、蛇、馬、羊、猴、雞、狗、豬'
print(chinese_zodiac[0:4] )
print(chinese_zodiac[-1])
year = 2018
print(year % 12)
print(chinese_zodiac[year % 12])
print('狗' not in chinese_zodiac )
print(chinese_zodiac + chinese_zodiac)
print(chinese_zodiac * 3)

#元组的操作
xz = ('1','2','3','4','5')
days = ((1,20),(2,20),(3,20),(4,20),(5,20))
(xx, yaa ) = (2, 15)
days = filter(lambda x: x <=(xx,yaa),days)
print(days)
daysa = len(list(days)) % 12
print(xz[daysa])

#列表的操作
aaa_list = ['abc','def']
aaa_list.append('a')
print(aaa_list)
aaa_list.remove('def')
print(aaa_list)
