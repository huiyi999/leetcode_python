'''
Given a non-empty array nums containing only positive integers,
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
'''
from typing import List


class Solution:
    def canPartition2(self, nums: List[int]) -> bool:
        totalSum = sum(nums)

        if totalSum % 2 != 0:
            return False

        self.subsetSum = totalSum // 2
        self.memo = {}
        return self.backtrack(nums, 0, self.subsetSum)

    def backtrack(self, nums, idx, target):
        if target in self.memo:
            return self.memo[target]

        if target == 0:
            self.memo[target] = True

        else:
            self.memo[target] = False
            if target > 0:
                for i in range(idx, len(nums)):
                    if self.backtrack(nums, i + 1, target - nums[i]):
                        self.memo[target] = True
                        break

        return self.memo[target]

    def canPartition(self, nums: List[int]) -> bool:
        '''
            Args:数组是否可以分为两半
            nums: 数组
            Returns:布尔值
            '''
        total = sum(nums)
        if total % 2 == 1:
            return False
        total = int(total / 2)
        dp = [False] * (total + 1)
        dp[0] = True
        for num in nums:
            i = total
            while i >= num:
                dp[i] = dp[i] or dp[i - num]
                i -= 1
        return dp[total]


'''
Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

'''