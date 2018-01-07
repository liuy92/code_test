#-*-coding:utf-8-*-
import sys
import math

reload(sys)
sys.setdefaultencoding('utf8')

"""
改脚本主要是为了将整形顺序进行倒置
例：input  output
123    321
-123   -321
120    21
"""

def integerReverse(x):
    x_str = str(x)
    n = len(str(x_str))
    if x < 0:
        x_rever = '-'
        for i in range(1, n):
            x_rever += x_str[n - i]
    elif x > 0:
        x_rever = ''
        for i in range(n):
            x_rever += x_str[n - 1 - i]
    else:
        x_rever = 0
    return int(x_rever)

if __name__ == '__main__':
    print integerReverse(10)
    print math.log(2147483648, 2)