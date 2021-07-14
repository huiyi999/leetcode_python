'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
'''
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.tmp = []

        def dfs(perm, s):
            if not perm:
                self.ans.append(s)
            for i in perm:
                tmp = perm[:]
                tmp.remove(i)
                dfs(tmp, s + [i])

        dfs(nums, [])
        return self.ans

    def permute2(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return []
        n = len(nums)
        List = []
        temp = [0] * n

        def permute_recursive(nums, index, n):
            if index == n:
                List.append(temp[:])
                return
            for i in range(len(nums)):
                temp[index] = nums[i]
                permute_recursive(nums[:i] + nums[i + 1:], index + 1, n)

        permute_recursive(nums, 0, n)
        return List


'''
Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


'''
