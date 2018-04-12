#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

"""
使用递归函数的一些小的应用
"""

class mysum:
    def mysum1(self, arr):
        if not arr:
            return 0
        else:
            return arr[0] + self.mysum1(arr[1:])
    def mysum2(self, arr):
        return 0 if not arr else arr[0] + self.mysum2(arr[1:])
    def mysum3(self, arr):
        return 0 if len(arr) == 0 else arr[0] + self.mysum3(arr[1:])
    def reverse(self,arr):
        if len(arr) == 0:
            return
        print arr[-1]
        return self.reverse(arr[:-1])
"""
1. 当在类内定义一个新的对象时，该对象固定，即在函数调用时该对象对应数据固定（若类内递归，则递归函数必须包含可变的新的输入对象值）
2. 类内的赋值的任何对象名均会边为类的属性，包含函数
3. 当类内包含多个函数时，若不调用其中的函数（属性），则该函数不会执行。知道其被调用赋值
4. 类可以随时在类外新增类的属性和对象
5. 类内的对象对应不同的作用域/命名空间
"""

if __name__ == '__main__':
    res = mysum()
    print res.mysum1(range(5))
    print res.mysum2(range(5))
    print res.mysum3(range(5))
    print res.reverse(range(5))
    res.new = 4
    print res.new
