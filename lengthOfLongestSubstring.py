#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

"""
最长不包含重复元素的字符串
input: 'asavda'
output:'savd'
input: 'pwwkew'
output:'wke'
"""

def longestSub(s):
    """
    :param s:string
    :return: string
    """
    print '-' * 15, s
    n = len(s)
    if n < 2:
        return s
    star = [0] * n
    res = [1] * n
    max_longs = 1
    max_index = 0
    for i in range(1, n):
        j = 1
        while i-j >= star[i-1] and s[i-j] != s[i]:
            j += 1
        star[i] = max(0, i-j+1)
        print "i=",i, j,"\tj=",s[i-j+1], '\tstar=', star[i], '\ta=', s[i],'\tmax_str=',s[star[i]:i+1]
        res[i] = j
        if j > max_longs:
            max_longs = j
            max_index = i
    return s[star[max_index]:max_index+1],max_index+1-star[max_index]

if __name__ == "__main__":
    a = 'asavda'
    b = 'pwwkew'
    print longestSub(a)
    print longestSub(b)
    print longestSub('bbbb')