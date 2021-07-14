'''
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?
'''
import math

'''
测试数据N可以相当大，直接硬算是不可取的。可以观察到每遇到一个5末位就会多一个零（前面有用不完的偶数），每遇到一个25又多一个零……
'''


class Solution:
    def trailingZeroes(self, n: int) -> int:
        x = n // 5
        return x + self.trailingZeroes(x) if x else 0


def trailingZeros(n):
    count = 0
    i = 5
    while n / i >= 1:
        count += n // i
        i = i * 5
    return count


print(math.factorial(1))
print(math.factorial(2))
print(math.factorial(3))
print(math.factorial(4))
print(math.factorial(5))
print(math.factorial(6))
print(math.factorial(7))
print(math.factorial(8))
print(math.factorial(9))
print(math.factorial(10))
print(math.factorial(14))
print(math.factorial(15))
print(trailingZeros(3))
print(trailingZeros(5))
print(trailingZeros(0))
print(trailingZeros(92))
so=Solution()

'''

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0

'''
