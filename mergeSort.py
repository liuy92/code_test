#-*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

#归并排序

def mergeSort(nums):
    def sort1(l, low, high):
        if low > high:
            return
        else:
            mid = (low + high) / 2