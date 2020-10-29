# 切片
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l[0:5])
l1 = list(range(100))
print(l1[-15:])

# 迭代
for i, value in enumerate(['赵', '钱', '孙', '李']):
    print(i, value)

## 列表生成器
r1 = [x * x for x in range(1, 111) if x % 5 == 1]
r2 = [(x1 + 1) * x1 for x1 in range(1, 10) if x1 %3 == 0]
r3 = [2 * x2 for x2 in range(10, 101)]
print(r1)
print(r2)
print(r3)

mn = [m * 2 + n * n for m in range(1, 10) for n in range(10, 20)]
print(mn)
