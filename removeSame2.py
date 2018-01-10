#-*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

"""
remove duplicates from sort array
input: [1,1,1,2,3,3,3,4]
output:[1,1,2,3,3,4]
"""


def removeSame21(A, n):
    """
    :param A:list
    :param n: int
    :return: list
    """
    if n >= len(A):
        return len(A)
    else:
        i = 0
        l = 0
        result = []
        while i < len(A):
            if i == len(A) - 1 or (A[i] != A[i + 1] and i < len(A) - 1):
                j = 0
                while A[i] == A[i - j]:
                    j += 1
                l += min(n, j)
                result += [A[i]] * min(n, j)
            i += 1
        print result
        return l

def removeSame22(A, n):
    N = len(A)
    if n >= N:
        return N
    else:
        j = 0
        num = 0
        for i in range(N):
            if A[i] == A[j]:
                num += 1
                if num < n:
                    j += 1
                    A[j] = A[i]
            elif A[i] != A[j]:
                j += 1
                A[j] = A[i]
                num = 0
        print A[:j + 1]
        return j + 1



if __name__ == '__main__':
    A = [1, 1, 1, 2, 3, 3, 3, 4]
    n = 2
    print removeSame21(A, n)
    print removeSame22(A, n)