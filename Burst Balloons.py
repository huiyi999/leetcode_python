'''
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums.
You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins.
Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100


'''
from typing import List

'''
dp:
c[i][j] = max(c[i][j], self.dfs(nums, c, i, k - 1) + nums[i - 1] * nums[k] * nums[j + 1] + self.dfs(nums, c, k + 1, j))


'''


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for len_ in range(1, n + 1):
            for left in range(1, n - len_ + 2):
                right = left + len_ - 1
                for k in range(left, right + 1):
                    dp[left][right] = max(dp[left][right],
                                          dp[left][k - 1] + nums[left - 1] * nums[k] * nums[right + 1] + dp[k + 1][
                                              right])
        return dp[1][n]

    def maxCoins2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = [1] + [n for n in nums if n > 0] + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for w in range(2, n):
            for l in range(n - w):
                r = l + w
                border = nums[l] * nums[r]
                m = 0
                for mid in range(l + 1, r):
                    cur = dp[l][mid] + nums[mid] * border + dp[mid][r]
                    if cur > m:
                        m = cur
                dp[l][r] = m
        return dp[0][-1]


solution = Solution()
solution.maxCoins([3, 1, 5, 8])
solution.maxCoins([9, 76, 64, 21])

'''
Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

'''
