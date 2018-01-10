#-*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

"""
选择排序
"""

def chooseSort(nums):
    """
    :param nums:list
    :return: list
    """
    N = len(nums)
    for i in range(N):
        for j in range(i+1, N):
            if nums[j] < nums[i]:
                k = nums[i]
                nums[i] = nums[j]
                nums[j] = k
    return nums

if __name__ == '__main__':
    a = [4,2,8,4,9,2,1,3]
    print chooseSort(a)