'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''
from itertools import permutations
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(set(permutations(nums, len(nums))))

    def permuteUnique2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = []
        self.tmp = []

        def dfs(perm, s):
            if not perm:
                self.ans.append(s)
            for i in set(perm):
                tmp = perm[:]
                tmp.remove(i)
                dfs(tmp, s + [i])

        dfs(nums, [])
        return self.ans

    def permuteUnique3(self, nums: List[int]) -> List[List[int]]:

        result = []

        def helper(s, i, slate):
            if i == len(s):
                result.append(slate[:])
                return
            map = set()  # eleminate the using the same element in

            for pick in range(i, len(s)):

                if s[pick] in map:
                    continue
                else:
                    map.add(s[pick])
                    s[pick], s[i] = s[i], s[pick]
                    slate.append(s[i])
                    helper(s, i + 1, slate)
                    slate.pop()
                    s[pick], s[i] = s[i], s[pick]

        helper(nums, 0, [])

        return result


'''
Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2], [1,2,1], [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''
