#-*-coding:utf-8-*-
import sys
import numpy as np
import datetime
import itertools

reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append('C:/Users/Administrator/PyCharmProjects/test_study/algothem')
import BinarySearch as bs

def three_sum1(sum, list):
    result = []
    n = len(list)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if i + j + k == sum:
                    result.append([list[i], list[j], list[k]])
    return result

def three_sum2(sum, list):
    list.sort()
    n = len(list)
    result = []
    for i in range(n):
        for j in range(i + 1, n):
            if bs.BinarySearch(list[j+1:], sum - (list[i] + list[j])) >= 0:
                result.append([list[i], list[j], sum - (list[i] + list[j])])
    return result

def three_sum3(target, nums):
    nums.sort()
    nums_list = itertools.combinations(nums, 3)
    result = []
    for li in nums_list:
        if sum(li) == target and li not in result:
            result.append(li)
    return result

def three_sum(nums):
    result = []
    if len(nums) < 3:
        return result
    nums.sort()  # 先排序
    for i in range(0, len(nums)):
        j = i + 1
        k = len(nums) - 1
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # 注意跳过重复的数，不然全0的长list会超时
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum == 0:
                result.append((nums[i], nums[j], nums[k]))
                k -= 1
                j += 1
                while (nums[j] == nums[j - 1] and nums[k] == nums[k + 1] and j < k):
                    j += 1
            elif sum > 0:
                k -= 1
                while (nums[k] == nums[k + 1] and j < k):
                    k -= 1
            else:
                j += 1
                while (nums[j] == nums[j - 1] and j < k):
                    j += 1
    return list(set(result))

if __name__ == '__main__':
    list = np.random.randint(0, 1000, 1000)
    a = 1000
    t1 = datetime.datetime.now()
    r1 = three_sum1(a, list)
    t2 = datetime.datetime.now()
    print len(r1), str(t2-t1) #, r1
    r2 = three_sum2(a, list)
    t3 = datetime.datetime.now()
    print len(r2), str(t3-t2) #, r2
