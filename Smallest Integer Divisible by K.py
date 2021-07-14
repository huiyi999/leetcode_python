'''
Given a positive integer K, you need to find the length of the smallest positive integer N
such that N is divisible by K, and N only contains the digit 1.

Return the length of N. If there is no such N, return -1.

Note: N may not fit in a 64-bit signed integer.

假设K=113，显然从M=1111开始尝试，首先余数remainder= M % K =94。
又因为 M_next = 11111 = 10 * M + 1，
所以有 M_next % K = (10 * (M % K) + 1) % K。
后面所有依此类推，直到余数为0(说明找到解)或者余数出现重复(说明无解)。
'''


class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:

        if K % 2 == 0 or K % 5 == 0: return -1

        remainders = set()
        l = 1
        remainder = 1 % K
        while 1:
            remainder = (10 * remainder + 1) % K
            l += 1
            if remainder == 0:
                return l
            if remainder in remainders:
                return -1
            else:
                remainders.add(remainder)

        return -1

    def smallestRepunitDivByK2(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0: return -1

        remainders = set()
        l = 1
        remainder = 1 % K
        while remainder != 0 and remainder not in remainders:
            remainder = (10 * remainder + 1) % K
            l += 1
        if remainder == 0:
            return l
        else:
            return -1

'''
Example 1:

Input: K = 1
Output: 1
Explanation: The smallest answer is N = 1, which has length 1.
Example 2:

Input: K = 2
Output: -1
Explanation: There is no such positive integer N divisible by 2.
Example 3:

Input: K = 3
Output: 3
Explanation: The smallest answer is N = 111, which has length 3.

'''
