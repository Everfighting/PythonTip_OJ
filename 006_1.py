# coding=utf-8
# 输出100以内的所有素数，素数之间以一个空格区分
print ' '.join(str(key) for key in [x for x in xrange(2, 101) if 0 not in [x % d for d in xrange(2, x/2)]])