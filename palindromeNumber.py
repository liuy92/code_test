#-*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

"""
判断一个数字是否是回文数字，例给出121即回文数字，122即非回文数字
input：121
output：true
"""

def palindromNumber1(x):
    """
    :param x: int
    :return: boolen
    """
    if x < 0:
        return False
    s = str(x)
    l = len(s)
    flag = True
    for i in range(l / 2 + 1):
        if s[i] != s[l - 1 - i]:
            flag = False
    return flag

if __name__ == '__main__':
    print palindromNumber1(12344321)