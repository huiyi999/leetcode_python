from typing import List

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i, num in enumerate(nums):
            remaining = target - num
            for j, value in enumerate(nums):
                if value == remaining and i != j:
                    res.append(i)
                    res.append(j)
                    return res

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            try:
                return [i, nums[i + 1:].index(target - nums[i]) + i + 1]
            except:
                pass

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return ([i, j])


so = Solution()
print(so.twoSum([3, 3], 6))
