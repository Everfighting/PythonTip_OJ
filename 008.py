# coding=utf-8
# 给你一个list L, 如 L=[0,1,2,3,4], 输出L的中位数（若结果为小数，则保留一位小数）。
L = [0,1,2,3,4]
L = sorted(L)
n = len(L)
if n % 2 == 0:
    print (L[n/2-1]+L[n/2])/2.0
else:
    print L[n/2]