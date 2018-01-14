#-*-coding:utf-8-*-
import sys
import numpy as np
reload(sys)
sys.setdefaultencoding('utf8')

"""
获取列表对应形成的直方图中面积最大的值
input:[2,1,5,6,2,3]
output:10
"""

def largestRectangle1(l):
    N = len(l)
    if N == 0:
        return 0
    else:
        res = max(l)
        for i in range(N-1):
            resi = min(l[i:]) * (N-i)
            res = max(resi, res)
            for j in range(i+1, N):
                resi = min(l[i:j]) * (j-i)
                res = max(resi, res)
        return res

def largestRectangle2(heights):
    if not heights:
        return 0
    elif len(heights) == 1:
        return heights[0]
    i = 0
    ans = 0
    flag = False
    while i < len(heights) and not flag:
        while i < len(heights) - 1 and heights[i] <= heights[i + 1]:
            i += 1
        if i == len(heights) - 1:
            flag = True
        min_height = heights[i]
        for j in range(i, -1, -1):
            min_height = min(min_height, heights[j])
            ans = max(ans, min_height * (i - j + 1))
        i += 1
    return ans

if __name__ == '__main__':
    a = [2,1,5,6,2,3]
    print a
    print largestRectangle1(a)