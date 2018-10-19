#-*-coding:utf-8-*-
import sys
<<<<<<< HEAD
import datetime
=======

>>>>>>> 92c14350679df652bac52eaeef132d0e648bdf2a
reload(sys)
sys.setdefaultencoding('utf8')

"""
<<<<<<< HEAD
求取所给出的列表中每个元素对应的以其为末尾元素构成的顺序子列的长度
input: 1 4 6 2 8 9 7
output:1 2 3 2 4 5 4
input: 1 4 6 2 8 9 5
output:1 2 3 2 4 5 3
"""

def LIS1(arr):
    n = len(arr)
    res = [1] * n
    for i in range(1, n):
        mx_ind = 0
        mx_val = 0
        for j in range(i):
            if arr[j] < arr[i] and arr[j] > mx_val:
                mx_ind = j
                mx_val = res[j]
        res[i] = mx_val + 1
    return res, max(res)

def LIS2(arr):
    print '-' * 10, arr
    n = len(arr)
    res = [1] * n
    tmp = [arr[0]]
    tmp_n = 1
    for i in range(1, n):
        if arr[i] > tmp[-1]:
            tmp.append(arr[i])
            tmp_n += 1
        else:
            j = tmp_n - 1
            while j >= 0 and tmp[j] > arr[i]:
                j -= 1
            tmp[j+1] = arr[i]
        #print arr[i], tmp
        res[i] = len(tmp)
    return res, tmp

if __name__ == '__main__':
    a = [1,4,6,2,8,9,7]
    b = [1,4,6,2,8,9,5]
    c = [7,8,2,1,2,3,4]
    t1 = datetime.datetime.utcnow()
    print LIS1(a)
    t2 = datetime.datetime.utcnow()
    print LIS2(a)
    t3 = datetime.datetime.utcnow()
    print t2-t1, t3-t2
    #print LIS2(c)
=======
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
>>>>>>> 92c14350679df652bac52eaeef132d0e648bdf2a
