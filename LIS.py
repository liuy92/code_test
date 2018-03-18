#-*-coding:utf-8-*-
import sys
import datetime
reload(sys)
sys.setdefaultencoding('utf8')

"""
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