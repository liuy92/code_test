#-*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

"""
随机数组分别代表最高位。。。个位
考虑将数据+1 后返回数组
例：
input: [1,2,42]
output:[1,6,3]
"""

def plusOne1(digits):
    """
    :param digits:list
    :return: list
    """
    n = len(digits)
    sum = 1
    for i in range(n):
        sum += digits[i] * 10 ** (n - 1 - i)
    result = []
    while sum / 10 >= 0 and sum % 10 > 0:
        result += [sum % 10]
        sum /= 10
    result2 = []
    for i in range(len(result)):
        result2 += [result[len(result)-1-i]]
    return result2

#def plusOne2(digits):


if __name__ == '__main__':
    print plusOne1([1,2,42])