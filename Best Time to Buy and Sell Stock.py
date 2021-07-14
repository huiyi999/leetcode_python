'''

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)

        return max_profit

    def maxProfit2(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        min_price = 10001  # 10000
        max_profit = 0
        for x in prices:
            if x - min_price > max_profit:
                max_profit = x - min_price
            elif x < min_price:
                min_price = x
        return max_profit


so = Solution()
print(so.maxProfit([7, 1, 5, 3, 6, 4]))
print(so.maxProfit([7, 6, 4, 3, 1]))
print(so.maxProfit2([7, 1, 5, 3, 6, 4]))
print(so.maxProfit2([7, 6, 4, 3, 1]))
'''

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

'''
