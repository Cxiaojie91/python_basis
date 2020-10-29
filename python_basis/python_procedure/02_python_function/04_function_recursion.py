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
# 1到100的和的几种写法
# 累加
def sum(n):
    '''
    累加
    :return: 1+2+3+...+n=
    '''
    s = 0
    for i in range(1, n+1):
        s += i
    return s
def main():
    print(sum(100))
main()

# 迭代
def sum02(n):
    '''
    迭代
    :param n: 迭代次数
    :return: n+(n-1)+(n-2)+..+2+1=
    '''
    if n == 1:
        return 1
    else:
        return n + sum02(n-1)
def main2():
    print(sum02(101))
main2()

# 使用求和公式
def sum03(n):
    '''
    求和公式
    :param n: 第n项
    :return: n(n+1)/2=
    '''
    return n * (1 + n) / 2
def  main3():
    print(sum03(102))
main3()

# 最简洁的一行搞定
# print(sum(range(1, 101)))