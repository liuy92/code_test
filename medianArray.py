#-*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def medianArray(nums1, nums2):
    nums = nums1 + nums2
    nums.sort()
    n = len(nums)
    if n == 1:
        median = nums[0]
    elif n == 0:
        median = None
    elif n % 2 == 0:
        median = (nums[n / 2] + nums[n / 2 + 1]) / 2.0
    else:
        median = nums[n / 2]
    return median

print medianArray([1, 3], [2])
print medianArray([1,2], [3, 4])