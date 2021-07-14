'''


Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
'''
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = [0] * len(nums)
        res[0] = nums[0]
        for i in range(1, len(nums)):
            res[i] = max(res[i - 1] + nums[i], nums[i])
        return max(res)

    def maxSubArray2(self, nums: List[int]) -> int:
        allmax = nums[0]
        curmax = nums[0]
        for i in nums[1:]:
            if curmax + i > i:
                curmax = curmax + i
            else:
                curmax = i
            if curmax > allmax:
                allmax = curmax

        return allmax

    def maxSubArray3(self, nums: List[int]) -> int:
        maxSubarraySum = float('-inf')
        currentMax = 0
        for x in range(len(nums)):
            currentMax = max(nums[x], currentMax + nums[x])
            maxSubarraySum = max(maxSubarraySum, currentMax)
        print(currentMax)
        print(maxSubarraySum)
        return max(currentMax, maxSubarraySum)


'''
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-100000]
Output: -100000
'''
