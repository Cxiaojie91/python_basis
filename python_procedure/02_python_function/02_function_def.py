# # 求函数my_abs的绝对值
# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
# print(my_abs(-1010))
#
# # 求函数my_abs1的绝对值
# def my_abs1(x1):
#     if not isinstance(x1, (int, float)):
#         raise TypeError('bad operand type')
#     if x1 >= 0:
#         return x1
#     else:
#         return -x1
# print(my_abs1(11))
#
# # 函数返回多个值
# import math
# def move(mx, my, step, angle=0):
#     nx = mx + step * math.cos(angle)
#     ny = my -step * math.sin(angle)
#     return nx, ny
# mr =move(100, 100, 60, math.pi / 6)
# print(mr)

# 作业：请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程ax² + bx +c =0的两个解.

import math
def quadratic(a, b, c):
    qx = math.sqrt(b ** 2 - 4 * a * c)
    if a == 0:
        return ('除数不能为0')
    elif b ** 2 < 4 * a * c:
        return ('平方根应大于等于0')
    else:
        qx1 = (-b + qx) / 2 * a
        qx2 = (-b - qx) / 2 * a
        return qx1, qx2
print(quadratic(3, 5, 2))




