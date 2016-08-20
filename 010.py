# coding=utf-8
# 给你两个正整数a和b， 输出它们的最小公倍数
# 方法一 :filter筛选
print min(filter(lambda x: x % a == 0 and x % b == 0, range(max(a, b), a * b + 1)))

