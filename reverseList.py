#-*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

"""
给定一段区间，仅翻转该区间的数据
input: [3,6,8,3,6,2,6,4], 2, 5
output:[3,6,6,3,8,2,6,4]
"""

def reverseList(nums, s, e):
    if s > len(nums):
        return nums
    else:
        k = 1
        i = s
        if e >= len(nums):
            e = len(nums) - 1
        while i >= s and i < e - k:
            temp = nums[i]
            nums[i] = nums[e - 1]
            nums[e-1] = temp
            k += 1
            i += 1
        return nums

if __name__ == '__name__':
    a = [3,6,8,3,6,2,6,4]
    print reverseList(a, 2, 5)