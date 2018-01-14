#-*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

"""
围棋棋盘统计线所构成的正方形有多少个
input：3
output：5
"""

def suqareGo(n):
    sum = 0
    for i in range(n):
        sum += i * i
    return sum


if __name__ == '__main__':
    print suqareGo(3)