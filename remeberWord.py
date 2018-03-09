#-*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

"""
记单词：给出m个需要记忆的单词，让同学默写，默写出n个单词，若默写正确获得单词长度平方的分数。
n个单词中可能存在相同的词汇，只计算一次
input：[m, n], [remberword], [targetword]
output:score
"""

def remeberWord2(nums, remeberword, targetword):
    """
    :param nums: list, contaion m, n
    :param remeberword: list
    :param targetword: list
    :return: int
    """
    remeber = set(remeberword)
    interset = remeber.intersection(targetword)
    score = 0
    for wi in interset:
        score += len(wi) ^ 2
    return score

def remeberWord(nums, remeberword, targetword):
    target_num = nums[0]
    remeber_num = nums[1]
    score = 0
    remeberword.sort()
    targetword.sort()
    i = 0
    j = 0
    while i < target_num and j < remeber_num:
        print i, j, targetword[i], remeberword[j]
        if j == 0:
            if remeberword[j] == targetword[i]:
                score += len(remeberword[j]) ^ 2
                i += 1
                j += 1
            elif remeberword[j] > targetword[i]:
                i += 1
            else:
                j += 1
        elif remeberword[j] == remeberword[j-1]:
            j += 1
        else:

            if remeberword[j] == targetword[i]:
                score += len(remeberword[j]) ^ 2
                i += 1
                j += 1
            elif remeberword[j] > targetword[i]:
                i += 1
            else:
                j += 1
    return score

if __name__ == '__main__':
    target = ['listen', 'good', 'wheel', 'couple', 'down']
    remeber = ['good', 'good', 'well', 'done', 'down','listen', 'how']
    print remeberWord([5, 7], remeber, target)
    print remeberWord2([5, 7], remeber, target)