'''
Alex and Lee play a game with piles of stones.
There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.
The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.
Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.
This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

题目解析：DP问题
dp[i][j]: 从第i个石头到第 j 即 (i+l-1)个石头之间最大的对手得分差。
Alex取piles[i]时，Lee也保持最佳状态从[ i+1, j ]中取值
Alex取piles[j]时，Lee也保持最佳状态从[ i, j+1 ]中取值
'''
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        '''
        Alex can always take all odd piles or always take all even piles
        Since sum of all piles is odd then sum of all odd piles won't equals sum of all even piles,
        Alex could just take the bigger ones.
        '''
        return True


'''
dp[i][j] means the biggest number of stones you can get more than opponent picking piles in piles[i] ~ piles[j].
You can first pick piles[i] or piles[j].

If you pick piles[i], your result will be piles[i] - dp[i + 1][j]
If you pick piles[j], your result will be piles[j] - dp[i][j - 1]
So we get:
dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
We start from smaller subarray and then we use that to calculate bigger subarray.
'''


# Approach 2: 2D DP
def stoneGame2(self, p):
    n = len(p)
    dp = [[0] * n for i in range(n)]
    for i in range(n): dp[i][i] = p[i]
    for d in range(1, n):
        for i in range(n - d):
            dp[i][i + d] = max(p[i] - dp[i + 1][i + d], p[i + d] - dp[i][i + d - 1])
    return dp[0][-1] > 0


# Approach 3: 1D DP
def stoneGame(self, p):
    n = len(p)
    dp = p[:]
    for d in range(1, n):
        for i in range(n - d):
            dp[i] = max(p[i] - dp[i + 1], p[i + d] - dp[i])
    return dp[0] > 0
