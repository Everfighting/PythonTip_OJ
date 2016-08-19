# coding=utf-8
# 输出100以内的所有素数，素数之间以一个空格区分
for i in range(2,101):
    flag = 0 # 设置标识符
    for j in range(2,i/2): # 嵌套相除取余
        if (i % j == 0):
            flag = 1       # 符合质数条件则
    if (flag == 0):
	    print i,


