#-*-coding:utf-8-*-
#import sys

#reload(sys)
#sys.setdefaultencoding('utf8')

"""
该脚本主要为了计算所有可以组合出给定的target值的所有组合
1. 元素从candiadtes中获取
2. 元素可重复多个
input : [2,3,6,7], 7
output: [[2,2,3], [7]]
"""

def combineSum(candidates, target):
    """
    :param candidates:list set
    :param target: int
    :return: list
    """
    candidates.sort()
    result = []
    def getValue(cand, tar, start, valuelist):
        """
        :param cand: list
        :param tar: int
        :param start: int, the pocition of the cand
        :param valuelist:list
        :return: list
        从目标列表cand中，查询是否存在目标值tar
        1. 若tar == 0, 说明valuelist的和为tar
        2. 若tar != 0, 则将比tar小的数据cand[i]放入valulist中，并以tar-cand[i]为目标值迭代查询在cand中是否存在比起小的值，直到tar为0
        """
        N = len(cand)
        print(tar, valuelist, start, N)
        if tar == 0:
            print('--',valuelist)
            return result.append(valuelist)
        for i in range(start, N):
            print(tar, valuelist, cand[i])
            if tar >= cand[i]:
                print(tar, valuelist)
                getValue(cand, tar - cand[i], i, valuelist + [candidates[i]])
    getValue(candidates, target, 0, [])
    return result

if __name__ == '__main__':
    print combineSum([2,3,6,7], 7)