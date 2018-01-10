#-*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

"""
帕斯卡三角
input： 5
output：
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

def pascalTriangle(n):
    res = []
    for i in range(n):
        if i == 0:
            res.append([1])
        elif i == 1:
            res.append([1,1])
        else:
            li = res[i - 1]
            lj = [1]
            for j in range(1, i):
                print j
                lj.append(li[j] + li[j-1])
            lj.append(1)
            res.append(lj)
    return res

if __name__ == '__main__':
    print pascalTriangle(6)