#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

"""
本脚本主要是总结整理所有排序算法
"""

#快排
def qSort(arr):
    if len(arr) < 2:
        return arr
    else:
        left = []
        right = []
        for i in arr[1:]:
            if arr[0] >= i:
                left.append(i)
            else:
                right.append(i)
        return qSort(left) + [arr[0]] + qSort(right)

def qSort0(arr):
    if len(arr) < 2:
        return arr
    else:
        return qSort0([i for i in arr[1:] if i > arr[0]]) + [arr[0]] + qSort([i for i in arr[1:] if i < arr[0]])

#选择排序,每次找到其后所有的数据中的最小值，并和最小值交换
def chSort(arr):
    n = len(arr)
    print range(n)
    for i in range(n):
        min_v = arr[i]
        min_i = i
        for j in range(i, n):
            if arr[j] < min_v:
                #print 'arr[i] =', arr[i], 'arr[j] =', arr[j]
                min_v = arr[j]
                min_i = j
        print arr, 'i =', i, 'j =', min_i
        tmp = arr[i]
        arr[i] = arr[min_i]
        arr[min_i] = tmp
    return arr

#插入排序,找到当前元素在其位置前的所有的元素中所处的位置，并插入
def isSort(arr):
    n = len(arr)
    print range(n)
    for i in range(n):
        j = 0
        while j < i and arr[j] < arr[i]:
            j += 1
        print arr, 'j =', j, 'i =', i, 'arr[j] =', arr[j], 'arr[i] =', arr[i]
        if j < i:
            #print arr[0:j], [arr[i]], arr[j:i], arr[i+1:n]
            arr = arr[0:j] + [arr[i]] + arr[j:i] + arr[i+1:n]
    return arr

#希尔排序
def shellSort(arr, m):
    n = len(arr)
    h = 0
    while h < n/m:
        h = m*h +1
        print '-' * 15, h
    while h >= 1:
        print '-' * 20, h
        for i in range(h, n):
            for j in range(i, 0, -h):
                if arr[j] < arr[j-h]:
                    tmp = arr[j]
                    arr[j] = arr[j-h]
                    arr[j-h] = tmp
            print arr, 'j =', j, 'h =', h, 'arr[j] =', arr[j], 'arr[j-h] =', arr[j-h]
        h = h/m
    return arr

#二分查找排序
def srchSort(arr):
    def srch(k, lo, hi):
        if hi < lo:
            print lo
            return lo
        mid = lo + (hi - lo) / 2
        if k < arr[mid]:
            return srch(k, lo, mid-1)
        elif k > arr[mid]:
            return srch(k, mid+1, hi)
        else:
            print mid
            return mid
    srch(arr[0], 0, len(arr))


if __name__ == '__main__':
    a = [3,6,2,5,8,3,7,9,4]
    #print chSort(a)
    #print isSort(a)
    #print shellSort(a, 3)
    print srchSort(a)
    #print range(10, 2, -3)
