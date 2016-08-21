# coding=utf-8
# 给你一个正整数列表 L, 如 L=[2,8,3,50],
# 判断列表内所有数字乘积的最后一个非零数字的奇偶性,
# 奇数输出1,偶数输出0. 如样例输出应为0.
L = [2,8,3,50]
a, b = 0, 0
for i in L:
	while i % 2 == 0:
		a += 1
		i = i/2

	while i % 5 == 0:
		b += 1
		i = i/5
if a > b:
	print 0
else:
	print 1
