'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?

Constraints:
1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

'''
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return

        length = len(nums)
        if k > len(nums):
            k = k % len(nums)

        tmp = nums[length - k:]
        nums[k:] = nums[:length - k]
        nums[:k] = tmp
        print(nums)

        #  approach 2
        # prepend = nums[-k:]
        # nums[-k:], nums[0:0] = [], prepend

        #  approach 3
        # a = nums[len(nums) - k:]
        # a += nums[0: len(nums) - k]
        # nums[:] = a


solution = Solution()
solution.rotate([1, 2, 3, 4, 5, 6, 7], 3)
solution.rotate([-1, -100, 3, 99], 2)

'''
Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]'''
