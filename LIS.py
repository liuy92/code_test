#-*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

"""
对数组，计算数组中可获取的最长递增的子列的长度
input：[1,4,6,2,8,9,7]
output:5
"""

def longStr(target):
    """
    :param target:list
    :return: list
    """
    res = []
    mx = 0
    for i in range(len(target)):
        if target[i] > mx:
            res.append(target[i])
            mx = target[i]
    return res

def LIS1(target):
    n = len(target)
    res = [1] * n
    nLis = 1
    print '-', target
    for i in range(1, n):
        for j in range(i):
            if target[j] <= target[i]:
                res[i] = max(res[i], res[j] + 1)
        print i, res
        nLis = max(nLis, res[i])
    return nLis

def LIS(target):
    n = len(target)
    res = [1] * n
    def insert(tar, ni, v):
        if ni <= 0:
            ni = ni + 1
            tar[0] = v
            return
        lo = 0
        hi = ni - 1
        while lo < hi:
            mid = (lo + hi) / 2
            if v < tar[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        if lo >= ni:
            a[ni] = v
            ni += 1
        else:
            if a[lo] < v:
                a[lo + 1] = v
            else:
                a[lo] = v
    j = 0
    for i in range(n):
        insert(res, j, target[i])
        print res, j, target
    return j


if __name__ == '__main__':
    a = [1,4,6,2,8,9,7]
    print LIS(a)