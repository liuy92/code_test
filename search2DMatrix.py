#-*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

"""
给定矩阵和特殊值，查找这个数据在该矩阵中是否存在
这个矩阵无论从行还是列，数字都是从小打到排序的
input：
[
[1,3, 6],
[2,7,10],
[5,8,12]
], 4
output:False
"""

def searchMatrix(matrix, target):
    """
    :param matrix:list(list)
    :param target: int
    :return: booleen
    """
    nrow = len(matrix)
    if nrow == 0:
        return False
    ncol = len(matrix[0])
    print ncol
    if ncol == 0:
        return False
    i = 0
    j = 0
    flag = False
    if target < matrix[i][j]:
        return flag
    while i < nrow and j < ncol:
        if target == matrix[i][j]:
            print i, j
            return True
        if i == nrow - 1:
            if j < ncol - 1 and target >= matrix[i][j + 1]:
                j += 1
            else:
                print '+++',i,j
                return flag
        elif j == ncol - 1:
            if i < ncol - 1 and target >= matrix[i+1][j]:
                i += 1
            else:
                print '===',i,j
                return flag
        else:
            if target >= matrix[i][j+1] and (matrix[i][j+1] < matrix[i+1][j] or target < matrix[i+1][j]):
                j += 1
            elif target >= matrix[i+1][j] and (matrix[i+1][j] < matrix[i][j+1] or target < matrix[i][j+1]):
                i += 1
            else:
                print '---',i, j
                return flag



if __name__ == '__main__':
    print searchMatrix([[1,3,5],[4,7,9],[8,12,14]], 8)