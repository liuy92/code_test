#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

"""
寻找下一个排列
input:21543
output:23145
思路：
1. 从后向前迭代，找到前一个数字小于于后一个数字的位置
2. 将该位置数字替换为其后的所有的元素中大于该值的最小值，剩余元素从小到大排列
"""

def nextPermutation(target):
    """
    :param str: int/string
    :return: int/string
    """
    tar = [i for i in str(target)]
    n = len(tar)
    if n < 2:
        return target
    i = n - 2
    while i >= 0 and tar[i] >= tar[i+1]:
        i -= 1
    next = min([j if j > tar[i] else 'z' for j in tar[i+1:]])
    tafter = tar[i:]
    tafter.remove(next)
    tafter.sort()
    t = str(target)[:i] + next + '' .join(tafter)
    return t

if __name__ == '__main__':
    print nextPermutation(21543)