# # 定义一个求平方的函数
# def power(x):
#     return x**2
# print(power(44))

# 定义一个求n次方的函数
def power1(x1, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x1
    return s
print(power1(101))

# 定义一个注册函数
def enroll(name,gender):
    print('name:', name)
    print('gender:', gender)
print(enroll('xiaojie', 'f'))

# 定义一个存在默认参数的注册函数
def enroll1(name1, gender1, age = 6, city = 'beijing'):
    print('name:', name1)
    print('gender:', gender1)
    print('age:', age)
    print('city:', 'beijing')
print(enroll1('chenxiaojie', 'F', 8))

