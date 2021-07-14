from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                return nums[i]

    def singleNumber2(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return nums[0]
        counter = Counter(nums)
        rev_counter = {v: k for k, v in counter.items()}
        return rev_counter[1]


'''
Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1


'''
