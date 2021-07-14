from typing import List


class Solution:
    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                count += 1
            else:
                i += 1
        for i in range(count):
            nums.append(0)

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[j - count] = nums[j]
            else:
                count += 1
        for i in range(count):
            nums[-1 - i] = 0
        print(nums)


so = Solution()
so.moveZeroes([0, 1, 0, 3, 12])
'''

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
'''
