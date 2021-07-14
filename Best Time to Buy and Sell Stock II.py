'''
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        buy, sell = -prices[0], 0  # profit for buy or sell
        for i in range(1, len(prices)):
            buy = max(buy, sell - prices[i])  #the max profit, if buy on this day
            sell = max(sell, buy + prices[i]) #the max profit, if sell on this day
        return sell
