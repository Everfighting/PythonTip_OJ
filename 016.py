# coding=utf-8
# 银行在打印票据的时候，常常需要将阿拉伯数字表示的人民币金额转换为大写表示，现在请你来完成这样一个程序。
# 在中文大写方式中，0到10以及100、1000、10000被依次表示为：
# 零壹贰叁肆伍陆柒捌玖拾佰仟万
# 以下的例子示范了阿拉伯数字到人民币大写的转换规则：
# 1	壹圆
# 11	壹拾壹圆
# 111	壹佰壹拾壹圆
# 101	壹佰零壹圆
# -1000 负壹仟圆
# 1234567	壹佰贰拾叁万肆仟伍佰陆拾柒圆
# 现在给你一个整数a(|a|<100000000), 打印出人民币大写表示.
# 注意：请以Unicode的形式输出答案。
# 你可以通过decode("utf8")来将utf8格式的字符串解码为Unicode，
# 例如你要输出ans = "零圆", print ans.decode("utf8").
a =123456
count = 1
neg = False
zero = False
s = '圆'
d = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
if a == 0:
    print '零圆'
else:
    if a < 0:
        neg = True
        a = -a
    while a > 0:
        if a % 10 == 0:
            if not zero and s != '圆':
                s = '零' + s
                zero = True
            a /= 10
            count += 1
            continue
        if count == 2:
            s = '拾' + s
        elif count == 3:
            s = '佰' + s
        elif count == 4:
            s = '仟' + s
        elif count == 5:
            s = '万' + s
            count -= 4
        s = d[a % 10] + s
        a /= 10
        count += 1
        zero = False
    if neg:
        s = '负' + s
    print s.decode("utf8")