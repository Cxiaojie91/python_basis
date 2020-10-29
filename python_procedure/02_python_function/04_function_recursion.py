# def hanoi(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
#     else:
#         hanoi(n - 1, a, c, b)
#         print(a, '-->', c)
#         hanoi(n - 1, b, a, c)
# # 调用
# hanoi(5, 'A', 'B', 'C')

# sum = 0
# for i in range(1, 101):
#     sum = sum + i
# print(sum)

# 阶乘
def fact(f):
    if f == 1:
        return 1
    return f * fact(f - 1)
print(fact(10))

