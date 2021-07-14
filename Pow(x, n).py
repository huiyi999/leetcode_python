'''

Implement pow(x, n), which calculates x raised to the power n (i.e. xn).



'''
import math


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return math.pow(x, n)  # return x**n

    def myPow2(self, x: float, n: int) -> float:

        def power(x, n):
            # print(count)
            if n == 0:
                return 1
            elif n == 1:
                return x
            b = power(x, n // 2)
            if n % 2 == 1:
                return b * b * x
            else:
                return b * b

        return 1 / power(x, -n) if n < 0 else power(x, n)

    def myPow3(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n == 1:
            return x
        elif n < 0:
            x = 1 / x
            n *= -1

        res = 1
        while n > 0:
            print(res,n)
            if n % 2 == 1:
                res *= x

            x *= x
            n = n // 2

        return res


so = Solution()
print(so.myPow3(2, 10))
print(so.myPow3(2, 3))

'''
Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

'''
