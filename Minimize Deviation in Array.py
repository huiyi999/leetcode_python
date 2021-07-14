'''
hard
You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

If the element is even, divide it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
If the element is odd, multiply it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.

Constraints:

n == nums.length
2 <= n <= 105
1 <= nums[i] <= 109

'''
import heapq
from typing import List

'''
For each a in A,
divide a by 2 until it is an odd.
Push divided a and its original value in to the pq.

The current max value in pq is noted as ma.
We iterate from the smallest value in pq,
Update res = min(res, ma - a),
then we check we can get a * 2.

If a is an odd, we can get a * 2,
If a < a0, which is its original value, we can also get a*2.

If we can, we push [a*2,a0] back to the pq and continue this process.
'''


class Solution:
    def minimumDeviation3(self, nums: List[int]) -> int:
        maxv = max(nums)
        ans = float('inf')
        heapq.heapify(nums)
        while True:
            ans = min(ans, maxv - nums[0])
            if nums[0] % 2 == 1:
                v = heapq.heappop(nums)
                maxv = max(maxv, v * 2)
                heapq.heappush(nums, v * 2)
            else:
                break
        nums = [-n for n in nums]
        maxv = max(nums)
        heapq.heapify(nums)
        while True:
            ans = min(ans, maxv - nums[0])
            if nums[0] % 2 == 0:
                v = heapq.heappop(nums)
                maxv = max(maxv, v // 2)
                heapq.heappush(nums, v // 2)
            else:
                break
        return ans

    def minimumDeviation2(self, A):
        pq = []
        for a in A:
            heapq.heappush(pq, [a / (a & -a), a])
        res = float('inf')
        ma = max(a for a, a0 in pq)
        while len(pq) == len(A):
            a, a0 = heapq.heappop(pq)
            res = min(res, ma - a)
            if a % 2 == 1 or a < a0:
                ma = max(ma, a * 2)
                heapq.heappush(pq, [a * 2, a0])
        return int(res)

    # deviation_min = float('inf')
    #
    # def minimumDeviation(self, nums: List[int]) -> int:
    #     # print(max([1,2]))
    #     num_max = max(nums)
    #     num_min = min(nums)
    #
    #     self.deviation_min = num_max - num_min
    #     print(self.deviation_min)
    #
    #     if num_max == num_min:
    #         return self.deviation_min
    #     elif num_max % 2 != 0 and num_min % 2 != 0:
    #         for i in range(len(nums)):
    #             if nums[i] == num_min:
    #                 nums[i] = nums[i] * 2
    #         self.minimumDeviation(nums)
    #     elif num_max % 2 == 0 and num_min % 2 == 0:
    #         for i in range(len(nums)):
    #             if nums[i] == num_max:
    #                 nums[i] = nums[i] // 2
    #         self.minimumDeviation(nums)
    #     elif num_max % 2 == 0 and num_min % 2 != 0:
    #         for i in range(len(nums)):
    #             if nums[i] == num_max:
    #                 nums[i] = nums[i] // 2
    #         self.minimumDeviation(nums)
    #     else:
    #         return self.deviation_min
    #     return self.deviation_min


so = Solution()
# print(so.minimumDeviation([1, 2, 3, 4]))
# print(so.minimumDeviation([4, 1, 5, 20, 3]))
# print(so.minimumDeviation([2, 10, 8]))
print(so.minimumDeviation([3, 5]))

'''
Example 1:

Input: nums = [1,2,3,4]
Output: 1
Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.
Example 2:

Input: nums = [4,1,5,20,3]
Output: 3
Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.
Example 3:

Input: nums = [2,10,8]
Output: 3

'''
