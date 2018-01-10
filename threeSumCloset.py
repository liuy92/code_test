#-*-coding:utf-8-*-
import sys
import itertools

reload(sys)
sys.setdefaultencoding('utf8')

"""
该脚本是给定一个列表找到3个该列表组合中的数据和同目标值差距最小的数据值
input: [-1, 2, 1, -4], 1
output: [-1, 1, 2] 2
"""

def threeCloset1(nums, target):
    """
    :param nums: list
    :param target: int
    :return: int
    """
    num_list= itertools.combinations(nums, 3)
    sum_list = []
    diff_list = []
    for li in num_list:
        sum_list.append(sum(li))
        diff_list.append(abs(sum(li) - target))
    result = dict(zip(diff_list, sum_list))
    return result[min(diff_list)]

def threeCloset2(nums, target):
    N = len(nums)
    if N < 3:
        return -1
    else:
        nums.sort()
        distance = 99999999999999999999999999999999999999
        res = 0
        for i in range(N - 2):
            j = i + 1
            k = N - 1
            while j < k:
                sumi = nums[i] + nums[j] + nums[k]
                if sumi < target:
                    diffi = target - sumi
                    if diffi < distance:
                        distance = diffi
                        res = sumi
                    j += 1
                elif sumi > target:
                    diffi = sumi - target
                    if diffi < distance:
                        distance = diffi
                        res = sumi
                    k -= 1
                else:
                    return sumi
        return sumi

if __name__ == '__main__':
    nums = [-1,2,1,-4]
    target = 1
    print threeCloset1(nums, target)
    print threeCloset2(nums, target)