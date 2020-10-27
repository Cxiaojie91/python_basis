# names = ['zhao', 'qian', 'sun', 'li']
# for name in names:
#     print(name)
#
# sum = 0
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     sum = sum + x
#     print(sum)
#
# sum1 = 0
# for x in range(101):
#     sum1 = sum1 + x
#     print(sum1)
#
# sum2 = 0
# n = 99
# while n > 0:
#     sum2 = sum2 + n
#     n = n - 2
#     print(sum2)
#
# L = ['Bart', 'Lisa', 'Adam']
# for l1 in L:
#     L = 'Hello ' + l1
#     print(L)

# n = 1
# while n <= 100:
#     if n > 10:
#         break
#     print(n)
#     n = n + 1
# print('End')

n1 = 0
while n1 < 100:
    n1 = n1 + 1
    if n1 % 2 == 0:
        continue
    print(n1)