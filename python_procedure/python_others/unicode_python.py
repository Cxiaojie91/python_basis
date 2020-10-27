print('包含文中的str')
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print(len(b'ABCDE'))

# 第一行告诉Linux/OS系统，这是一个Python可执行程序，Windows会忽略该注释
# 第二行是告诉Python解释器，按照UTF-8编码读取源代码，否则中文的输出有可能会乱码
#！/usr/bin/env python3
# -*- coding:utf-8 -*-
# -*- coding: utf-8 -*-
s1 = 72
s2 = 85
r = (s2 - s1)/s1*100
#print(r)
print('小明成绩提升：%.1f%%' % r)
print('小明成绩提升：{0:.1f}%'.format(r))
print(f'小明成绩提升：{r:.1f}%')