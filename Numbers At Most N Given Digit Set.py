'''
Given an array of digits, you can write numbers using each digits[i] as many times as we want.
For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.

Return the number of positive integers that can be generated that are less than or equal to a given integer n.

Constraints:
1 <= digits.length <= 9
digits[i].length == 1
digits[i] is a digit from '1' to '9'.
All the values in digits are unique.
1 <= n <= 109
'''
from typing import List
''' 
（1）假设数字 N 为 K 位， 很显然，K-1 的数字一定比它小, 能组成 K-1 位的数有为(K-1)^(len(D))，
（2）现在位数为 K，其比 N 小的数字 动态规划方法:
    从数据集D中依次拿出 一个数去和N的最高位比较，如果比它小，后面各个位上的数字可以任意组合，通过求次方就可以得到。
    如果比它大，很显然，后面再怎么组合也是不符合要求的，所以直接舍弃。 
    如果相等，那么就可以直接等于次高位符合要求的个数（形成子问题 – 动态规划的一个必要条件）。然后把所有的累加，就是位数为 K 且小于N的数字个数。

'''

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        S = str(n)
        K = len(S)
        dp = [0] * K + [1]
        print(dp)
        for i in range(K - 1, -1, -1):
            for d in digits:
                if d < S[i]:
                    dp[i] += len(digits) ** (K - i - 1)
                elif d == S[i]:
                    dp[i] += dp[i + 1]
        print(dp)
        return dp[0] + sum(len(digits) ** i for i in range(1, K))


solution = Solution()
print(solution.atMostNGivenDigitSet(["1", "3", "5", "7"], 100))
print(solution.atMostNGivenDigitSet(["1","4","9"], 1000000000))

'''
 

Example 1:

Input: digits = ["1","3","5","7"], n = 100
Output: 20
Explanation: 
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
Example 2:

Input: digits = ["1","4","9"], n = 1000000000
Output: 29523
Explanation: 
We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
In total, this is 29523 integers that can be written using the digits array.
Example 3:

Input: digits = ["7"], n = 8
Output: 1

'''
