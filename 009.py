# coding=utf-8
# 方法一 ：辗转相除法

a = min(a, b)
b = max(a, b)
while a != 0:
	b, a = a, b % a

print b


# 方法二：迭代法
def func(a, b):
	if a % b == 0:
		return b
	return func(b, a % b)

print (func(a, b))