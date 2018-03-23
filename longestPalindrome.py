#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

"""
求最长的回文字符串
input: babad
output:bab
"""

def longestPal(s):
    """
    :param s:string
    :return: string
    """
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return s
    s1 = '#' + '#'.join(list(s)) + '#'
    print '-' * 15, s, s1
    n = len(s1)
    res = [1] * n
    dis = 1   #最远距离
    j = 0     #最远距离对应中心位置
    i = 1     #迭代位置
    max_palin = 1   #最长回文串对应的数据位置
    while dis < n:
        if i < dis:
            res[i] = min(dis-i, res[2*j-i])
        while i+res[i] < n and s1[i+res[i]] == s1[i-res[i]]:
            res[i] += 1
        if i + res[i] > dis:
            dis = i + res[i]
            j = i
        if res[i] > max_palin:
            max_palin = res[i]
            max_index = i
        #if s1[i] != '#':
        print 'i=', i, '\ta=', s1[i], '\tlen=', res[i], '\tres=', s1[i-res[i]+1:res[i]+i]
        i += 1
    return s1[max_index-max_palin+1:max_index+max_palin].replace('#','')

if __name__ == '__main__':
    a = 'ababcas'
    b = 'abbacac'
    print longestPal(a)
    print longestPal(b)