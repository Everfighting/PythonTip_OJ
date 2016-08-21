# coding=utf-8
# 给你一字典a，如a = {1: 1, 2: 2, 3: 3}，输出字典a的key
# 以','链接，如‘1, 2, 3'
a = {1: 1, 2: 2, 3: 3}

# 迭代器访问
# 列表解析式和join方法，参数是str instance
print ",".join([str(x) for x in a])

# 若key为字符串类型
# print ",".join(a.keys())