#-*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

"""
该脚本主要是计算manachar算法
即分别计算在一定长度的list中，以每个元素为中心的堆成序列的长度是多少，即每个元素对应回文长度
思想：
1. 考虑回文的形式可能有两种：奇数长度和偶数长度，为便于处理，可在所有的元素中间插入特殊符号使每个元素都存在回文且长度均大于1
2. 数学归纳法：
   假定已知前 k-1 个元素的回文长度，来计算第 k 个元素对应的回文长度。
   前 k-1 个元素中，第i个元素所涉及的回文串的距离是最远的，回文长度为l
   若 k < i+1 即k在第i个元素的对称范围内，可以找到其对称点 2i - k，则k的最短回文长度为 min(p[2i-k], i+l-k)
   若 k > i+l 暴力求解
3. 注意2所求的只是k的由前面所得的最短回文长度，需要以 目前的长度 p[k] 继续迭代查看其实质的最长的回文长度
   即 迭代查看 第 k-p[k] 和 k+p[k]的元素是否相同，不同停止，求出实际上k位置的最长回文长度

计算复杂度为 o(n)
input: bacabacac
output:113141221
       012345678
"""

def Init(target):
    tar = str(target)
    res = '#'
    for i in tar:
        res = res + str(i) + '#'
    return res

def manacher(target):
    tar = Init(target)
    maxlen = -1
    mx = 0
    p = []
    res = []
    id = 0
    for i in range(len(tar)):
        if i < mx:
            p.append(min(mx - i, p[2*id - i]))
        else:
            p.append(1)
        p1 = p[i]
        while i+p[i] < len(tar) and tar[i-p[i]] == tar[i+p[i]]:
            p[i] += 1
        p2 = p[i]
        if mx < i + p[i]:
            mx = i + p[i]
            id = i
        maxlen = max(maxlen, p[i])
        if tar[i] != '#':
            print str(i/2) + '\t' + tar[i] + '\tp1 =' + str(p1) + '\tp2 = ' + str(p2/2) + '\tmaxlen = ' + str(maxlen/2)
            res.append(p2/2)
    return max(res), res

if __name__ == '__main__':
    print manacher('bacabacac')