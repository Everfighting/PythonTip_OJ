# coding=utf-8
# 给你个小写英文字符串a和一个非负数b(0<=b<26), 将a中的每个小写字符替换成字母表中比它大b的字母。
# 这里将字母表的z和a相连，如果超过了z就回到了a。
# 例如a="cagy",b=3, 则输出 fdjb

res = []
for x in a:
    res.append(chr(((ord(x)-ord('a')+b)%26)+ord('a')))
print ''.join(res)