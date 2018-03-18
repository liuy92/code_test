#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

"""
已知股票的历史价格，为保证收益最大，确定买入时间和卖出时间
input:[4,2,6,3,7,3,2,1,2,6,8,6,7]
output:7
"""
def maxDiff1(arr):
    mx_val = arr[0]
    mi_val = arr[0]
    mx_diff = 0
    res = [0]
    for i in range(1, len(arr)):
        if arr[i] > mx_val:
            mx_diff = max(mx_diff, arr[i] - mi_val)
            mx_val = arr[i]
        elif arr[i] < mi_val:
            mi_val = arr[i]
            mx_val = arr[i]
        res.append(mx_diff)
        print i, arr, res
    return res, mx_diff

if __name__ == '__main__':
    a = [4,2,6,3,7,3,2,1,2,6,8,6,7]
    print maxDiff1(a)