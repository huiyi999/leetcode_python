'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


'''


class Solution:
    def climbStairs1(self, n: int) -> int:
        '''
        复杂度分析，时间复杂度为2^n。
        因为有重复的数据多次计算，比如f(3), 每个大于3的都要重新计算一次。
        递归函数还有个弊端，需要担心函数调用栈溢出。

        '''
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs1(n - 1) + self.climbStairs1(n - 2)

    def climbStairs2(self, n: int) -> int:
        '''递推公式：f(n) = f(n-1) + f(n-2)'''
        if n == 1:
            return 1
        elif n == 2:
            return 2
        stairs = [0] * (n + 1)
        stairs[1] = 1
        stairs[2] = 2
        for i in range(3, n + 1):
            stairs[i] = stairs[i - 1] + stairs[i - 2]
        return stairs[-1]

    def climbStairs(self, n: int) -> int:
        stairs = [0] * n
        stairs[0] = 1
        if n == 1:
            return stairs[0]
        stairs[1] = 2
        for i in range(2, n):
            stairs[i] = stairs[i - 1] + stairs[i - 2]
        return stairs[n - 1]


so = Solution()
print(so.climbStairs2(2))
print(so.climbStairs2(3))
print(so.climbStairs2(4))
print(so.climbStairs2(5))
print(so.climbStairs2(6))

'''
Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

'''
