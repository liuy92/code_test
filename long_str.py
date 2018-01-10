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

def longStr2(s):
    dic, res, start, = {}, 0, 0
    for i, ch in enumerate(s):
        print i, ch
        if ch in dic:
            print i, ch
            # update the res
            res = max(res, i-start)
            # here should be careful, like "abba"
            start = max(start, dic[ch]+1)
        dic[ch] = i
    # return should consider the last
    # non-repeated substring
    return max(res, len(s)-start)



#print longStr("abcabcbb")
#print longStr("bbbbb")
#print longStr("pwwkew")
print longStr("dvdf")