#-*-coding:utf-8-*-
import sys
import numpy as np
reload(sys)
sys.setdefaultencoding('utf8')
"""
已知股票价格的历史记录，假设我们可以买卖k次，只允许卖完后买入，来确定最大收益
input:
思路：
第i天的最大收益，只有两种选择：卖出、不卖出
若不卖出：则该天的最大收益和前一天的最大收益相同，即：dp[k,i]=dp[k,i-1]
若卖出：  则改天的最大收益，其实是第i-1天前的k-1次最大的收益加上k-1次最大收益后当前价格-最低价格
         或最后一次买入的最大收益+（现在价格-最后一次买入的价格）
注：在使用动态规划或者相同的题目时，需要考虑的是发生变化的是两个参数：历史最佳买入卖出时间和卖出次数
    则题目其实是两个维度，分别是卖出次数和最佳收益
    难度在于构建状态转移方程
"""
def maxEarning(arr, K):
    res = np.array([[0] * len(arr)] * (K+1))
    for k in range(1, K+1):
        for i in range(1,len(arr)):
            #print k, i, len(res), res[k][i]
            res[k][i] = res[k][i-1]
            for j in range(i):
                res[k][i] = max(res[k][i], res[k-1][j] + arr[i]-arr[j])   #分别记录迭代找到不同购买次数对应的截止当前的最大收益，而最大收益值区分不卖出时和前个状态相同，卖出时，找到最佳的买入时间j，做价格相减
            print "截止第",i,"天第",k,"次买卖的最大收益：",res[k][i], res
    return res[K][len(arr) - 1], res

def maxEarning2(arr, K):
    res = np.array([[0] * len(arr)] * (K+1))
    for k in range(1,K+1):
        mx = res[k-1][0] - arr[0]
        for i in range(1, len(arr)):
            res[k][i] = max(res[k][i-1], mx + arr[i])
            mx = max(mx, res[k-1][i] - arr[i])
            print "截止第", i, "天第", k, "次买卖的最大收益：", res[k][i], res
    return res[K-1][len(arr)-1], res


if __name__ == '__main__':
    arr = [2,1,5,3,6,4,5,7,1,5,6,3,9]
    print maxEarning(arr, 3)
    print maxEarning2(arr, 3)