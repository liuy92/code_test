#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

"""
Fibonacci数列，即list[n] = list[n-1] + list[n-2]
感觉递归就像是数学归纳法的应用，只需要知道已知的数据，推新数据
"""

#循环思想
def FibonacciFor(n):
    a = [1, 1]
    for i in range(2, n+1):
        a.append(a[i-1] + a[i-2])
    return a[n]

#递归思想
def FibonacciRec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return FibonacciRec(n-1) + FibonacciRec(n-2)



if __name__ == '__main__':
    print FibonacciFor(5)
    print FibonacciRec(5)