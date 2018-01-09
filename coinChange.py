#-*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def change(amount, coins):
    """
    :type amount: int
    :type coins: List[int]
    :rtype: int
    """
    coins.sort()
    final = []
    def lessList(lists, a):
        i = 0
        result = []
        while i <= len(lists) - 1 and lists[i] <= a:
            #print i
            result.append(lists[i])
            i += 1
        return result
    coins1 = lessList(coins, amount)
    for i in range(1, len(coins1) + 1):
        result = []
        csi = coins1[:i]
        #print '==' * 10, csi, amount
        def maxSum(cs, am):
            coinsi = lessList(cs, am)
            max_a = max(coinsi)
            #print max_a, result
            #print sum(result)
            if amount % max_a == 0:
                result.append(max_a)
            else:
                while am % max_a != 0 and sum(result) < amount:
                    am -= max_a
                    coinsi = lessList(coinsi, am)
                    result.append(max_a)
                    try:
                        maxSum(coinsi, am)
                    except:
                        return []
        while sum(result) < amount:
            maxSum(csi, amount)
        if sum(result) == amount:
            #print '++' * 10, i, result
            final.append(result)
    return len(final)

#动态规划:总额为i时的方案数 = 总额为i-coins[j]的方案数的加和.
def coinChange(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:
        for x in range(c, amount + 1):
            dp[x] += dp[x - c]
            print '-' * x, x, c, dp
    return dp[amount]

if __name__ == '__main__':
    #print lessList([1], 5)
    print coinChange([1,2,5], 5)