#-*-coding:utf-8-*-
import sys
import numpy as np

reload(sys)
sys.setdefaultencoding('utf8')

#该脚本主要是通过二分法找到某数据在列表中所在的位置

def BinarySearch0(list, a):
    min_value = 0
    max_value = len(list) - 1
    while max_value >= min_value:
        j = min_value + (max_value - min_value) / 2
        #print '======', list[j], a
        if a > list[j]:
            min_value = j + 1
        elif a < list[j]:
            max_value = j - 1
        else:
            return j
    return min_value

def BinarySearch1(arr, a):
    def srch(lo, hi):
        if lo > hi:
            return lo
        mid = lo + (hi - lo) / 2
        if a > arr[mid]:
            return srch(a, mid+1, hi)
        elif a < arr[mid]:
            return srch(a, lo, mid-1)
        else:
            return mid
    srch(0, len(arr))

def BinarySearch(arr, a):
    lo = 0
    hi = len(arr) -1
    while lo < hi:
        mid = (lo + hi) / 2
        if arr[mid] > a:
            hi = mid - 1
        elif arr[mid] < a:
            lo = mid + 1
        else:
            return mid
    return lo



if __name__ == '__main__':
    list = np.random.randint(0, 1000, size = 1000)
    a = int(np.mean(list))
    list.sort()
<<<<<<< HEAD
    #print list
    print BinarySearch([1], 0)
=======
    print list
    print BinarySearch0([0], 0)
>>>>>>> 44d259251691ac42dabc84ba74468f91878f4381
