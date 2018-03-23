#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

"""
递归法逆推
"""

def sss(ll):
    def ss(i):
        if i == 0:
            print i, ll[i]
            return 0
        else:
            print i, ll[i]
            return ss(i-1)
    ss(len(ll) - 1)
sss([1,2,34])