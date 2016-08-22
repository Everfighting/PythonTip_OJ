# coding=utf-8
# 我们经常遇到的问题是给你两个数，要你求最大公约数和最小公倍数。
# 今天我们反其道而行之，给你两个数a和b，计算出它们分别是哪两个数的最大公约数和最小公倍数。
# 输出这两个数，小的在前，大的在后，以空格隔开。
# 若有多组解，输出它们之和最小的那组。
# 注：所给数据都有解，不用考虑无解的情况。

sum=a*b
for x in range(a+1,b-1):        #a+1遍历到b-1，其实只要遍历到（a+b)/2就可以了把？
    if x%a == 0 and b%x==0:
        y=(a*b)/x               #这是x,y对于最大公约数和最小公倍数的关系
        if(x+y < sum):          #找出和最小的一对并记录下来
            sum=x+y
            flag_a=x
            flag_b=y
if flag_a<flag_b:
    print flag_a,flag_b
else:
    print flag_b,flag_a
