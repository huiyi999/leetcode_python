'''
Given an integer array nums, return the number of longest increasing subsequences.

Constraints:
0 <= nums.length <= 2000
-106 <= nums[i] <= 106
'''
from typing import List


class Solution:
    '''
    要求个数，首先还是得求最长的长度
    dp_len[i]表示以nums[i]结尾的最长递增子序列的长度
    dp_count[i]表示以nums[i]结尾的最长递增子序列的个数

    求最长长度的方法：遍历nums[i]之前的所有数，找到所有nums[j]<nums[i]，最长的dp_len[j]+1就是dp_len[i]
    求最长长度时的个数的方法: 遍历所有dp_len[j]，其中0<=j<i，依然只关注nums[i]>nums[j]的情况
        如果dp_len[j]>= dp_len[i] ，那么dp_count[i] = dp_count[j] 。
        如果dp_len[j]== dp_len[i] - 1，那么dp_count[i]+=dp_count[j]
    '''
    def findNumberOfLIS(self, nums: List[int]) -> int:

        # longest increasing subsequences
        dp_len = [1] * len(nums)
        dp_count = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    # dp_len[i] = max(dp_len[i],dp_len[j] + 1)
                    if dp_len[j]>=dp_len[i]:
                        dp_count[i] = dp_count[j]
                        dp_len[i] =dp_len[j] + 1
                    elif dp_len[j]== dp_len[i] - 1:
                        dp_count[i] += dp_count[j]

        print(dp_count)
        print(max(dp_count))
        return sum(dp_count[i] for i in range(len(nums)) if dp_len[i]==max(dp_len))




solution = Solution()
print(solution.findNumberOfLIS([1, 3, 5, 4, 7]))
print(solution.findNumberOfLIS([2, 2, 2, 2, 2]))
print(solution.findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2]))  # Expected: 3  12347 12457 12357
print(solution.findNumberOfLIS([1, 2]))  # Expected: 1
'''
Example 1:
Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:
Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, 
and there are 5 subsequences' length is 1, so output 5.
'''
