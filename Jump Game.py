'''

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.


'''
from typing import List


class Solution:
    def canJump3(self, nums: List[int]) -> bool:
        m = 0

        for i, n in enumerate(nums):
            if m < i:
                return False
            m = max(m, i + n)
        return True

    def canJump2(self, nums: List[int]) -> bool:
        end = len(nums) - 1
        cur = end - 1
        while cur >= 0:
            if nums[cur] >= end - cur:
                end = cur
            cur -= 1
        return end == 0

    def canJump(self, nums: List[int]) -> bool:
        max_step = nums[0]
        for i in range(1, len(nums)):
            if max_step < i:
                break
            if i + nums[i] > max_step:
                max_step = i + nums[i]
        return True if max_step >= len(nums) - 1 else False


# def canJump(self, nums: List[int]) -> bool:
#  TLE
# print(len(nums))
# if len(nums) == 1:
#     return True
#
# def dfs(index):
#     # if index > len(nums) - 1:
#     #     return False
#     if index == len(nums) - 1:
#         return True
#     max_step = nums[index]
#     if max_step == 0:
#         return False
#     if max_step >= len(nums) - 1 - index:
#         return True
#     for i in range(1, max_step + 1):
#         if dfs(index + i):
#             return True
#     return False
#
# return dfs(0)
'''
贪心算法：
1.贪心算法中，作出的每步贪心决策都无法改变，因为贪心策略是由上一步的最优解推导下一步的最优解，而上一部之前的最优解则不作保留。
2.由（1）中的介绍，可以知道贪心法正确的条件是：每一步的最优解一定包含上一步的最优解

动态规划算法:
1.全局最优解中一定包含某个局部最优解，但不一定包含前一个局部最优解，因此需要记录之前的所有最优解
2.动态规划的关键是状态转移方程，即如何由以求出的局部最优解来推导全局最优解
3.边界条件：即最简单的，可以直接得出的局部最优解

本题用一个数 reach 表示能到达的最远下标，一步步走下去，如果发现在 reach 范围之内某处能达到的范围大于 reach，
那么我们就用更大的范围来替换掉原先的 reach，这样一个局部的最优贪心策略，在全局看来也是最优的，
因为 局部能够到达的最大范围也是全局能够到达的最大范围

'''

so = Solution()
print(so.canJump([2, 3, 1, 1, 4]))
print(so.canJump([3, 2, 1, 0, 4]))
print(so.canJump([3, 0, 8, 2, 0, 0, 1]))  # true

print(so.canJump(
    [2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9, 6, 8, 8, 0, 6, 3, 1, 2, 2, 1, 2, 6, 5, 3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0, 0,
     3, 8, 2, 4, 0, 1, 2, 0, 1, 4, 6, 5, 8, 0, 7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4, 3, 7, 0, 4, 9, 0, 9, 8, 4, 3, 0, 7, 7,
     1, 9, 1, 9, 4, 9, 0, 1, 9, 5, 7, 7, 1, 5, 8, 2, 8, 2, 6, 8, 2, 2, 7, 5, 1, 7, 9, 6]))

'''
Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

'''
