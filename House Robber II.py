'''
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected,
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 1000

Hide Hint #1
Since House[1] and House[n] are adjacent, they cannot be robbed together.
Therefore, the problem becomes to rob either House[1]-House[n-1] or House[2]-House[n],
depending on which choice offers more money. Now the problem has degenerated to the House Robber, which is already been solved.
'''
from typing import List


class Solution:
    '''
    appraoch 2:16ms
    '''
    def rob2(self, nums: List[int]) -> int:
        def rob(nums):
            now = prev = 0
            for n in nums:
                now, prev = max(now, prev + n), now
            return now

        return max(rob(nums[len(nums) != 1:]), rob(nums[:-1]))

    '''
        appraoch 1: 32ms
    '''
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        max_mount1 = self.startrob(nums, 0, len(nums) - 1)
        max_mount2 = self.startrob(nums, 1, len(nums))
        return max(max_mount1, max_mount2)

    def startrob(self, nums, start, end):
        max_mount = 0
        before1 = 0
        before2 = 0
        # print(nums[start:end])
        for num in nums[start:end]:
            max_mount = max(before1, num + before2)
            before2 = before1
            before1 = max_mount
        return max_mount


solution = Solution()
print(solution.rob([2, 3, 2]))  #3
print(solution.rob([1, 2, 3, 1])) #4
print(solution.rob([0]))  #0
print(solution.rob([5]))  #5
print(solution.rob([]))  #0

'''
Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [0]
Output: 0
'''
