#-*-coding:utf-8-*-
import sys
import numpy as np

reload(sys)
sys.setdefaultencoding('utf8')

#该脚本主要是通过二分法找到某数据在列表中所在的位置

def BinarySearch(list, a):
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

if __name__ == '__main__':
    list = np.random.randint(0, 1000, size = 1000)
    a = int(np.mean(list))
    list.sort()
    print list
    print BinarySearch([0], 0)
