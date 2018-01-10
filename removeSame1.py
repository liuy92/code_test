#-*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

"""
remove duplicates from sorted array
example:
input: A = [1,1,2]
return :[1,2]
"""

def removeSame11(A):
    """
    :param A: list
    :return: list
    """
    result = []
    i = 0
    j = 0
    if i == len(A):
        return 0
    else:
        while i < len(A):
            if i == 0:
                result.append(A[i])
                j += 1
            elif A[i] != A[i - 1]:
                result.append(A[i])
                j += 1
            i += 1
        print result
        return j

def removeSame12(A):
    j = 0
    for i in range(len(A)):
        if A[j] != A[i]:
            j += 1
            A[j] = A[i]
    print A[: j + 1]
    return j + 1

if __name__ == '__main__':
    print removeSame12([1, 1, 2, 2, 3, 4, 5, 6, 6, 8])
    print removeSame11([1, 1, 2, 2, 3, 4, 5, 6, 6, 8])

