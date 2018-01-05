#-*-coding:utf-8-*-
import sys
import numpy as np
import datetime

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
