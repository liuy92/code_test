#-*-coding:utf-8-*-
import sys
import numpy as np
reload(sys)
sys.setdefaultencoding('utf8')

"""
编写一颗简单的决策树，数据格式为一个字典，每个字典的主键代表第几个样本，key对应该样本下的特征对应的数据的字典
"""

class decisionTree:
    def __init__(self, df):
        self.data = df
        self.feature = fea
        self.label = list(set([df[i]['y'] for i in df]))
    #定义不纯度
    def getEnt(self, di):
        ni = len(di)
        count = {}
        for ki in di:
            li = di[ki]['y']
            if li not in di.keys():
                count[li] = 0
            count[li] += 1
        entropy = 0
        for ki in count:
            pi = float(count[ki]) / ni
            entropy -= pi * np.log(pi)
        return entropy
    def getGini(self,di):
        ni = len(di)
        count = {}
        for ki in di:
            li = di[ki]['y']
            if li not in di.keys():
                count[li] = 0
            count[li] += 1
        gini = 0
        for ki in count:
            pi = float(count[ki]) / ni
            gini += pi * (1-pi)
        return gini
    #进行数据分隔,二分类
    def splitData(self, di, fi, thre):
        less = []
        high = []
        less_label = 0
        high_label = 0
        for dij in di:
            if di[dij][fi] <= thre:
                less.append(dij)
                less_label.append(di[dij]['y'])
            else:
                high.append(dij)
                high_label.append(di[dij]['y'])
        less_rate = float(sum([1 for i in less_label if i == self.label[0]])) / len(less_label)
        high_rate = float(sum([1 for i in high_label if i == self.label[0]])) / len(high_label)
        if less_rate >= high_rate:
            pre = float((sum([1 for i in less_label if i == self.label[0]]) + sum([1 for i in high_label if i == self.label[1]]))) / len(di)
            return less, high, self.label[0], self.label[1], pre
        else:
            pre = float((sum([1 for i in less_label if i == self.label[1]]) + sum(
                [1 for i in high_label if i == self.label[0]]))) / len(di)
            return less, high, self.label[1], self.label[0], pre
    #选择最优阈值
    def threChood(self, di, fi):
        thres = [di[i][fi] for i in di]
        thres.sort()
        max_pre = 0
        thre = thres[0]
        for thi in thres:
            less, high, less_label, high_label, pre = self.splitData(di, fi, thi)
            if pre > max_pre:
                thre = thi
        return thre
    #循环迭代找出最优的feature
    def getFea(self, di):
        ni = len(di)
        entro0 = self.getEnt(di)
        for fi in self.feature:
            best_thre = self.threChood(di, fi)
            less, high, fi_less_label, fi_less_label, pre = self.splitData(di, fi, best_thre)
            entro1 = float(len(less)) / ni * self.getEnt(less) + float(len(high)) / ni * self.getEnt(high)
            if entro0 < entro1:
                less_max = less
                high_max = high
                less_label = fi_less_label
                high_label = fi_less_label
                feat = fi
                entro0 = entro1
        return less_max, high_max, less_label, high_label, feat, entro1
    #递归构建决策树
    def tree(self, oridata, ):



if __name__ == '__main__':
    df = {1: {'y':0, 'f1':5, 'f2': 1, 'f3': 0},
          2: {'y':0, 'f1':4, 'f2': 1, 'f3': 2},
          3: {'y':0, 'f1':2, 'f2': 0, 'f3': 1},
          4: {'y':0, 'f1':5, 'f2': 4, 'f3': 3},
          5: {'y':1, 'f1':3, 'f2': 3, 'f3': 2},
          6: {'y':1, 'f1':2, 'f2': 4, 'f3': 6},
          7: {'y':1, 'f1':0, 'f2': 5, 'f3': 5},
          8: {'y':1, 'f1':1, 'f2': 3, 'f3': 2}
          }
    fea = ['f1', 'f2', 'f3']
