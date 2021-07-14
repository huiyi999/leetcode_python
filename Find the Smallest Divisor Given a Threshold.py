'''
Given an array of integers nums and an integer threshold,
we will choose a positive integer divisor and divide all the array by it
and sum the result of the division.
Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

It is guaranteed that there will be an answer.

Constraints:
1 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 10^6
nums.length <= threshold <= 10^6
'''
import math
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # print(math.ceil(7 / 3))
        # print(math.ceil(1 / 3))
        # print(math.ceil(10 / 2))
        # print(math.ceil(2 / 4))


        #  Brute Force:  Time Limit Exceeded

        divisor_l = 1
        divisor_r = max(nums)

        while divisor_l != divisor_r:

            mid = (divisor_l + divisor_r) // 2
            print("mid: ", mid)
            result = 0
            for num in nums:
                print("math.ceil(num / mid): ",math.ceil(num / mid))     # nums=array(nums)  if sum(ceil(nums/mid))>threshold:
                result += math.ceil(num / mid)
            print("result: ", result)
            if result <= threshold:
                divisor_r = mid
            else:
                divisor_l = mid + 1

        print("divisor: ", divisor_l)
        return divisor_l


solution = Solution()
solution.smallestDivisor([1, 2, 5, 9], 6)
solution.smallestDivisor([2, 3, 5, 7, 11], 11)
solution.smallestDivisor([19], 5)
'''
Example 1:
Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1.
If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2).

Example 2:
Input: nums = [2,3,5,7,11], threshold = 11
Output: 3

Example 3:
Input: nums = [19], threshold = 5
Output: 4
'''
