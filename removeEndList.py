#-*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def removeEndList(head, n):
    """
    :param head: listNode
    :param n:  int
    :return:  listnode
    """
    j = len(head) - n
    head.pop(j)
    return head

if __name__ == '__main__':
    print removeEndList([1,2,3,4,5], 2)