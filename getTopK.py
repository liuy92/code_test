#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

"""
给定一个无序的列表，求解topk个元素输出
input: [1,3,6,3,4,7,9],3
output:[6,7,9]
"""

def qSort(arr):
    if len(arr) > 0:
        return qSort([i for i in arr[1:] if i <= arr[0]]) + \
           [arr[0]] + qSort([i for i in arr[1:] if i >= arr[0]])
    else:
        return arr

def qSort1(arr):
    if len(arr) <= 1:
        print '1.' ,arr
        return arr
    elif len(arr) > 1:
        k = arr[0]
        left = []
        right = []
        for i in arr[1:]:
            if i > k:
                left.append(i)
                print 'i =', i , 'left =', left
            else:
                right.append(i)
                print 'i =', i,'right =', right
        print 'k=',k,'left=',left,'right=',right
        #print left, qSort1(left)
        return qSort1(left) + [k] + qSort1(right)


def getTop(arr, k):
    if len(arr) <= k:
        return arr
    else:
        res = [arr[0]]
        for i in arr[1:]:
            j = 0
            while j < len(res) and res[j] > i:
                j += 1
            print 'i =', i, 'j =', j, 'res =', res, 'left =',len(res[0:j]), 'right =',len(res[j:k-1])
            res = res[0:j] + [i] + res[j:k-1]
        return res



if __name__ == '__main__':
    a = [4,2,5,1,7,6,3,7]
    print getTop(a,4)