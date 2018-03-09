#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

"""
已知历史股票收益变化，求出什么时候买入、卖出的收益最大
input：[3,5,9,4,1,4,6,8,5,4]
output:7
"""

def maxEarn(target):
    lo = 0
    hi = len(target) - 1
    mx = target[hi]
    mi = target[lo]
    res = mx - mi
    print target
    while lo < hi:
        #"""
        if target[hi] < target[hi-1]:
            print '=' * 20, 'if'
            mx = target[hi - 1]
            res = max(res, mx - mi)
            hi -= 1
        elif target[lo + 1] < target[lo]:
            print '=' * 20, 'elif'
            mi = target[lo + 1]
            res = max(res, mx - mi)
            lo += 1
        else:
            print '=' * 20, 'else'
            #"""
            i = 0
            while i + lo < hi and target[i + lo] >= target[lo]:
                print '-', target[i + lo] , target[lo], res
                i += 1
            lo += i
            mi = min(target[lo], mi)
            res = max(res, mx - mi)
            j = 0
            while hi - j > lo and target[hi - j] <= target[hi]:
                print '+', target[hi - j] , target[hi], res
                j += 1
            hi -= j
            mx = max(target[hi], mx)
            res = max(res, mx - mi)
        print 'low = ', lo, '\thight = ', hi, '\tmin_value = ', mi, '\tmax_value = ', mx, res
    return res, mx, mi

if __name__ == '__main__':
    target = [3,5,9,4,1,4,6,8,5,4]
    print maxEarn(target)
