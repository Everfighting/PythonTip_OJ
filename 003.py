# coding=utf-8
# 解法一：切片
a='12345'
print a[::-1]
# 解法二：转化成列表倒序+字符串连接
print ''.join(sorted(list(a),reverse=True))