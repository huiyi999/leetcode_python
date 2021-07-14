'''
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part.
For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For this problem, assume that your function returns 231 − 1 when the division result overflows.


'''


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0 or abs(dividend) < abs(divisor):
            return 0
        # elif divisor == 1:
        #     if dividend > 2 ** 31 - 1:
        #         return 2 ** 31
        #     elif dividend < -2 ** 31:
        #         return -2 ** 31
        #     else:
        #         return dividend
        # elif divisor == -1:
        #     if -dividend > 2 ** 31 - 1:
        #         return 2 ** 31 - 1
        #     elif -dividend < -2 ** 31:
        #         return -2 ** 31
        #     else:
        #         return -dividend
        # elif dividend == divisor:
        #     return 1
        # elif dividend == -divisor:
        #     return -1

        quotient = 0
        sign = 1
        if (dividend < 0 and divisor > 0) or (divisor < 0 and dividend > 0):
            sign *= -1
        dividend, divisor = abs(dividend), abs(divisor)

        while dividend >= divisor:
            val, count = divisor, 1
            while val + val <= dividend:
                val += val
                count += count

            quotient += count
            dividend -= val

        if sign == 1:
            return min(quotient, 2 ** 31 - 1)
        else:
            return max(-quotient, -2 ** 31)


so = Solution()
print(so.divide(-2147483648, -1))
print(so.divide(10, 3))
print(so.divide(7, -3))
print(so.divide(0, 1))
print(so.divide(1, 1))

'''
Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Example 3:

Input: dividend = 0, divisor = 1
Output: 0
Example 4:

Input: dividend = 1, divisor = 1
Output: 1

'''
