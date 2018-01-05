#-*-coding:utf-8-*-
import sys
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
reload(sys)
sys.setdefaultencoding('utf8')

def binormalCounter(n):
    list = np.random.randint(0, 2, n)
    n0 = 0
    n1 = 0
    for i in list:
        #print i
        if list[i] == 0: n0 += 1
        else: n1 += 1
    #print '成功', n1, '\t失败', n0
    return n1 * 1.0 / n

if __name__ == '__main__':
    r = []
    for i in np.random.randint(1000, 10000, 1000):
        ri = binormalCounter(i)
        print ri
        r.append(ri)
    sns.kdeplot(np.array(r), shade = True)
    plt.show()