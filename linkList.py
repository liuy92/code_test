#-*-coding:utf-8-*-
#import sys

#reload(sys)
#sys.setdefaultencoding('utf8')

#构建链表
class Node:
    def __init__(self, initdata):
        self._data = initdata
        self._next = None
    def getData(self):
        return self._data
    def getNext(self):
        return self._next
    def setData(self, newdata):
        self._data = newdata
    def setNext(self, newnext):
        self._next = newnext

class linkList:
    def __init__(self):
        self.head = Node(None)   #设置头结点，头结点的下个指针指向链表的head
        self.head.setNext(self.head)
    def add(self, item):
        temp = Node(item)  #增加节点，节点内容为item，节点的指针位置指向下个节点
        temp.setNext(self.head.getNext())
        self.head.setNext(temp)   #新增的元素为头结点指针指向的位置
    def remove(self, item):
        prev = self.head
        while prev.getNext() != self.head:  #迭代循环做查找，并查看每个元素指针指向元素是否为item，如果是，则该指针指向指向元素的下个位置
            cur = prev.getNext()
            if cur.getData() == item:
                prev.setNext(cur.getNext())
            prev = prev.getNext()
    def search(self, item):
        cur = self.head.getNext()
        while cur != self.head:
            if cur.getData() == item:
                return True
            cur = cur.getNext()
        return False
    def empty(self):
        return self.head.getNext() == self.head()
    def size(self):
        count = 0
        cur = self.head.getNext()
        while cur != self.head:
            cur += 1
            cur = cur.getNext()
        return count


"""
链表相加
input：2-4-3， 5-6-4
output:7-0-8
"""
def addLink(node1, node2):
    h1 = node1.head.getNext()
    h2 = node2.head.getNext()
    print h1, h2
    res = linkList()
    carry = 0
    while h1 != None & h2 !=None:
        value = h1 + h2 + carry
        carry = value / 10
        value %= 10
        res.add(value)
        h1 = node1.head.getNext()
        h2 = node2.head.getNext()
    return res

if __name__ == '__main__':
    node1 = linkList()
    node2 = linkList()
    for i in [4,6,8,3]:
        node1.add(i)
    for j in [6,2,4]:
        node2.add(j)
    print addLink(node1, node2)
