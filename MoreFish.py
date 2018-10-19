#-*-coding:utf-8-*-
import sys
import random

reload(sys)
sys.setdefaultencoding('utf8')

"""
好多鱼：
一个鱼缸n条鱼，每条鱼体积为l[i]，若鱼A体积为B的2~10倍，会吃掉B
给定新入鱼的体积范围，问多少条鱼不会被吃，也不会吃别的鱼(不考虑已有鱼的竞争关系)
input:新入鱼体积范围，鱼缸鱼的数量，鱼缸鱼的体积
output：可放入的鱼的数量
"""

def moreFish(newSize, oldSize):
    """
    :param newSize:list,contaion minSize and maxSize
    :param oldSize:list,contain all size
    :return:list
    """
    res = []
    oldSize.sort()
    print oldSize
    N = len(oldSize)
    for l in range(newSize[0], newSize[1] + 1):
        danger_l = range(int(l/10), int(l/2)+1) + range(int(l*2), int(l*10) + 1)
        if len(set(danger_l).intersection(oldSize)) == 0:
            res.append(l)
    return res

def moreFish2(newSize, oldSize):
    res = []
    oldSize.sort()
    N = len(oldSize)
    print oldSize, N
    for l in range(newSize[0], newSize[1] + 1):
        i = 0
        j = 0
        while j < N and i == 0:
            if (l * 1.0 / 10 <= oldSize[j] and oldSize[j] <= l * 1.0 / 2.0) or (l * 2 <= oldSize[j] and oldSize[j] <= l * 10):
                i = 1
            j += 1
        if i == 0:
            res.append(l)
    return res

if __name__ == '__main__':
    a = [1, 1000]
    b = random.sample(range(1000), 20)

    print moreFish(a, b)
    print moreFish2(a, b)