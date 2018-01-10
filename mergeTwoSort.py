#-*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

"""
给定两个排序的list，合并后进行排序
input : [1,5,6], [2,5,8,9]
output:[1,2,5,5,6,8,9]
"""

def mergeSort1(l1, l2):
    l = l1 + l2
    l.sort()
    return l

def mergeSort2(l1, l2):
    i = 0
    j = 0
    result = []
    while i + j < len(l1) + len(l2) and i <= len(l1) and j <= len(l2):
        if i < len(l1) and j < len(l2) and l1[i] <= l2[j]:
            result.append(l1[i])
            i += 1
        elif i < len(l1) and j < len(l2) and l1[i] > l2[j]:
            result.append(l2[j])
            j += 1
        elif i >= len(l1):
            result.append(l2[j])
            j += 1
        elif j >= len(l2):
            result.append(l1[i])
            i += 1
    return result

if __name__ == '__main__':
    l1 = [1, 5, 6]
    l2 = [2, 5, 8, 9]
    print mergeSort1(l1, l2)
    print mergeSort2(l1, l2)