#-*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

#选择字符串中最长的连续唯一出现的字符串
def longStr(s):
    n = len(s)
    max_n = 0
    for i in range(n):
        j = i + 1
        li = s[i]
        while j < n and s[j] not in li:
            li += s[j]
            j += 1
        ni = len(li)
        max_n = max([ni, max_n])
    return max_n

"""
思路：
从开始遍历
1. 如果出现和之前相同的元素，则起始位置从 前一个元素的位置+1 和 起始位置中最大的元素 选择
2. 随时计算最长距离 ：当前最大的位置 和 当前位置-起始位置 中最长的位置
"""
def longStr2(s):
    dic, res, start, = {}, 0, 0
    for i, ch in enumerate(s):
        print '=====', s[start:i], dic
        if ch in dic:
            print i, ch, dic[ch]+1, start
            # update the res
            res = max(res, i-start)
            # here should be careful, like "abba"
            start = max(start, dic[ch]+1)
        dic[ch] = i
    # return should consider the last
    # non-repeated substring
    return max(res, len(s)-start)



print longStr2("abcabcbb")
#print longStr2("bbbbb")
#print longStr2("pwwkew")
#print longStr2("dvdf")