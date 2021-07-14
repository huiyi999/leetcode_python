'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

两个递推公式来分别更新两个变量local和global，我们其实可以求至少k次交易的最大利润，找到通解后可以设定 k = 2，即为本题的解答。
定义local[i][j]为在到达第i天时最多可进行j次交易并且最后一次交易在最后一天卖出的最大利润，此为局部最优。
然后我们定义global[i][j]为在到达第i天时最多可进行j次交易的最大利润，此为全局最优。
它们的递推式为：
local[i][j] = max(global[i - 1][j - 1] + max(diff, 0), local[i - 1][j] + diff)
global[i][j] = max(local[i][j], global[i - 1][j])
'''


class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        # l = [[0, 0, 0] * len(prices)]  #对[1][1] 进行更换值, [0][1],[2][1]也会变，原因是浅拷贝，我们以这种方式创建的列表，list_two 里面的三个列表的内存是指向同一块，不管我们修改哪个列表，其他两个列表也会跟着改变。
        # g = [[0, 0, 0] * len(prices)]
        l = [[0 for i in range(3)] for j in range(len(prices))]
        g = [[0 for i in range(3)] for j in range(len(prices))]

        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            for j in range(1, 3):
                l[i][j] = max(g[i - 1][j - 1] + max(diff, 0), l[i - 1][j] + diff)
                g[i][j] = max(g[i - 1][j], l[i][j])
        return g[-1][-1]


'''
Example 1:
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.'''
