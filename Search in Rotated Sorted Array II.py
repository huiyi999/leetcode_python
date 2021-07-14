'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
'''
from typing import List


class Solution:
    def search2(self, nums: List[int], target: int) -> bool:
        if target in nums:
            return True
        else:
            return False

    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False

        low = 0
        high = len(nums) - 1

        while low < high:
            mid = int(low + (high - low) / 2)
            if nums[mid] == target:
                return True
            elif nums[low] < nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[low] > nums[mid]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                low += 1
        if nums[low] == target:
            return True
        return False

    def search3(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[end]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            elif nums[mid] < nums[end]:

                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid
            else:
                end -= 1

        if nums[start] == target:
            return True
        if nums[end] == target:
            return True

        return False


'''
Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

'''
