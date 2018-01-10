#-*-coding:utf-8-*-
import sys
import numpy as np

reload(sys)
sys.setdefaultencoding('utf8')

#该脚本主要是找到列表中连续出现相同的元素后进行消除，类似开心消消乐
"""
A = ['a','a','b','b','b','c','c','c','a','c']
return ['c']
"""

#计算元素连续出现的长度
def calSame(array):
    n_array = len(array)
    result_same = []
    for i in range(n_array):
        a = array[i]
        if i > 0 and array[i] == array[i - 1]:
            result_same.append(result_same[i - 1])
        else:
            j = 0
            while i + j < n_array and array[i + j] == a:
                j += 1
            result_same.append(j)
    return result_same

#消除元素
def valRemove(array, result_same, n):
    dele_num = 0
    i = 0
    n_all = len(array)
    while dele_num + i < n_all:
        if result_same[i + dele_num] >= n:
            array.pop(i)
            dele_num += 1
        else:
            i += 1
        print array, i, dele_num, len(array)
    return array

def main(array, n):
    same_result = calSame(array)
    max_same = max(same_result)
    while max_same >= n:
        print '============', max_same, same_result
        array = valRemove(array, same_result, n)
        same_result = calSame(array)
        max_same = max(same_result)
    print array
    return array

if __name__ == '__main__':
    l = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'a', 'c']
    #l = ['b', 'b', 'b', 'c']
    main(l, 3)