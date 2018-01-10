#-*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def foreSum1(nums, target):
    N = len(nums)
    if N < 4:
        return -1
    else:
        nums.sort()
        diff = 9999999999999999999999
        res = 0
        for i in range(N - 3):
            for j in range(i+1, N - 2):
                m = j + 1
                k = N - 1
                while m < k:
                    sumi = nums[i] + nums[j] + nums[k] + nums[m]
                    if sumi < target:
                        diffi = target - sumi
                        if diffi < diff:
                            diff = diffi
                            res = sumi
                        m += 1
                    elif sumi > target:
                        diffi = sumi - target
                        if diffi < diff:
                            diff = diffi
                            res = sumi
                        k += 1
                    else:
                        return target
        return res

