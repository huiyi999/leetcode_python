'''

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

'''
from typing import List


class Solution:
    '''
Explanation

For each bit, count how many numbers have 0 or 1 on that bit; the total difference on that bit is zero * one
zero: the amount of numbers which have 0 on bit i
one: the amount of numbers which have 1 on bit i
Sum up each bit, then we got the answer
Time Complexity: O(32*N) -> O(N)
    '''

    def totalHammingDistance2(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            zero = one = 0
            mask = 1 << i  # For each bit, count how many numbers have 0 or 1 on that bit
            for num in nums:
                if num & mask:
                    one += 1  # one: the amount of numbers which have 1 on bit i
                else:
                    zero += 1  # zero: the amount of numbers which have 0 on bit i
            ans += one * zero  # Sum up each bit, then we got the answer
        return ans

    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        count_ones = [0] * 31

        for num in nums:

            for i in range(31):
                count_ones[i] += (num >> i) & 1
        for count in count_ones:
            ans += count * (len(nums) - count)
        return ans


so = Solution()
print(so.totalHammingDistance([4, 14, 2]))

'''

Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
'''
