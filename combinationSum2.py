#-*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')
"""
该脚本主要是从目标列表中选择元素组合。使和为目标值
要求：每个元素只能出现一次
input:[10, 1, 2, 7, 6, 1, 5], 8
output:[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""

def combinationSum2(candidates, target):
    """
    :param candidates: list
    :param target: int
    :return: list  array<array>
    """
    #candidates.sort()
    result = []
    def getValue(cand, tar, start, valuelist):
        N = len(cand)
        valuelist.sort()
        if tar == 0 and valuelist not in result:
            result.append(valuelist)
        for i in range(start, N):
            print(candidates, tar, start, cand[i], valuelist, result)
            if tar >= cand[i]:
                getValue(cand, tar - cand[i], i + 1, valuelist + [cand[i]])
    getValue(candidates, target, 0, [])
    return result

if __name__ == '__main__':
    print combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)