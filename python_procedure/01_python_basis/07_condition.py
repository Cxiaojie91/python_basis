# a = 17
# if a >=18:
#     print('你的年龄是：', a)
#     print('你已成年')
# else:
#     print('你的年龄是：', a)
#     print('你未成年')
#
# b = 2
# if b >= 18:
#     print('adult')
# elif b >= 6:
#     print('teenager')
# elif b >= 3:
#     print('kid')
# else:
#     print('baby')
#
# s = input('birth:')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

# 作业
w = input('weight:')
h = input('height:')
weight = float(w)
height = float(h)
bmi = weight / (height * height)
if bmi < 18.5:
    print('过轻')
elif 18.5 <= bmi <= 25:
    print('正常')
elif 25 <= bmi <= 28:
    print('过重')
elif 28 <= bmi <= 32:
    print('肥胖')
else:
    print('严重肥胖')