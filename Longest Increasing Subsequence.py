'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

'''
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)

        if l == 0: return 0
        dp = [0] * l
        res = 0
        for i in range(l):
            max_len = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    max_len = max(max_len, dp[j])
                dp[i] = max_len + 1
                res = max(res, max_len + 1)

        return res

    '''
    faster approach
    '''

    def lengthOfLIS2(self, nums: List[int]) -> int:
        subseq = len(nums) * [0]
        last = -1
        for i, n in enumerate(nums):
            l = 0
            h = last
            while l <= h:
                mid = (l + h) // 2
                if nums[subseq[mid]] == nums[i]:
                    l = mid
                    break
                if nums[subseq[mid]] < nums[i]:
                    l = mid + 1
                else:
                    h = mid - 1
            subseq[l] = i
            if l > last:
                last = l
        return last + 1
