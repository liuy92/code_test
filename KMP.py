#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

"""
KMP算法主要是镜像字符串匹配
即：给定两个字符串 ，查看b字符串中是否包含a字符串，若包含，返回包含a的第一个位置

input：abcac, acbdabcddabcacaacabc
output:9
"""


def getNext(s):
    n = len(s)
    next = [-1]
    k = -1
    j = 0
    while j < n - 1:
        if k == -1 or s[j] == s[k]:
            k += 1
            j += 1
            next.append(k)
        else:
            k = next[k]
        print j, '\t', k, '\t', s[k], '\t', s[:j+1]
    return next


def kmpTest(a, b):
    i = 0
    j = 0
    while i != len(a) and b != len(b):
        print str(j) + '\tb[j] = ' + b[j] + '\ta[:i] = ' + a[:i+1]
        if a[i] != b[j]:
            i = 0
            j += 1
        else:
            i += 1
            j += 1
    return j - i

if __name__ == '__main__':
    a = 'abcac'
    b = 'acbdabcddabcacaacabc'
    #print kmpTest(a, b)
    for i, j in zip(getNext(b), b):
        print i, j