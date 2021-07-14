'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Notice that you may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Constraints:
0 <= k <= 109
0 <= prices.length <= 104
0 <= prices[i] <= 1000
'''
from typing import List


class Solution:
    #  time limited
    # def maxProfit(self, k: int, prices: List[int]) -> int:
    #     if k == 0 or len(prices) == 0: return 0
    #
    #     l = [[0 for i in range(k + 1)] for j in range(len(prices))]
    #     g = [[0 for i in range(k + 1)] for j in range(len(prices))]
    #
    #     for i in range(1, len(prices)):
    #         diff = prices[i] - prices[i - 1]
    #         for j in range(1, k + 1):
    #             l[i][j] = max(g[i - 1][j - 1] + max(diff, 0), l[i - 1][j] + diff)
    #             g[i][j] = max(g[i - 1][j], l[i][j])
    #     return g[-1][-1]

    def maxProfit2(self, k: int, prices: List[int]) -> int:
        from heapq import heapify, heappop

        if len(prices) < 2:
            return 0

        profits = []
        queue = []
        for i in range(1, len(prices)):
            p0, p1 = prices[i - 1], prices[i]
            if p1 <= p0:
                continue

            while queue:
                q0, q1 = queue[-1]
                if p0 < q0:
                    profits.append(q0 - q1)
                    queue.pop()
                else:
                    break

            while queue:
                q0, q1 = queue[-1]
                if q0 <= p0 and q1 < p1:
                    if p0 - q1 < 0:
                        profits.append(p0 - q1)
                    p0, p1 = q0, p1
                    queue.pop()
                else:
                    break

            queue.append((p0, p1))

        profits += [p0 - p1 for p0, p1 in queue]
        heapify(profits)

        answer = 0
        for _ in range(min(len(profits), k)):
            answer -= heappop(profits)
        return answer

        # Time: O(nk), Space: O(n+k)
        #
        # dp[i,k] = max(dp[j, k-1] - p[j]) + p[i]  for 0 <= j <= i
        # Keep track of max term as we go to turn quadratic into linear.
        # For each k, keep track of max profit and max diff.
        #
        # Optimization: for huge k - since max number of trades is bound by n/2,
        # if k exceeds n/2 just make all profitable transactions.

    def maxProfit3(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n / 2 <= k:
            return sum([max(prices[i + 1] - prices[i], 0) for i in range(n - 1)])

        dp = [[0, float('-inf')] for _ in range(k + 1)]  #float('-inf') 负无穷

        for price in prices:
            for j in range(1, k + 1):
                profit, maxDiff = dp[j]
                dp[j][0] = max(profit, maxDiff + price)
                dp[j][1] = max(maxDiff, dp[j - 1][0] - price)

        return dp[-1][0]


solution = Solution()
solution.maxProfit(2, [2, 4, 1])
solution.maxProfit(2, [3, 2, 6, 5, 0, 3])
solution.maxProfit(2, [3, 3, 5, 0, 0, 3, 1, 4])
solution.maxProfit(2, [1, 2, 4, 2, 5, 7, 2, 4, 9, 0])

'''
Example 1:
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

'''
