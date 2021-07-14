'''
Count the number of prime numbers less than a non-negative number, n.

'''
import math

'''
假如n是合数，必然存在非1的两个约数p1和p2，其中p1<=sqrt(n)，p2>=sqrt(n)。由此我们可以改进上述方法优化循环次数

质数分布的规律：大于等于5的质数一定和6的倍数相邻。例如5和7，11和13,17和19等等；

证明：令x≥1，将大于等于5的自然数表示如下：
··· 6x-1，6x，6x+1，6x+2，6x+3，6x+4，6x+5，6(x+1），6(x+1)+1 ···
'''


class Solution:

    def isPrime(self, num):
        if num <= 3:
            return num > 1
        # // 不在6的倍数两侧的一定不是质数
        if num % 6 != 1 and num % 6 != 5:
            return False
        sqrt = int(math.sqrt(num))
        for i in range(5, sqrt + 1, 6):
            if num % i == 0 or num % (i + 2) == 0:
                return False
        return True

    def isPrime2(self, num):
        if num % 6 != 1 and num % 6 != 5:
            return False
        # // Loop's ending condition is i * i <= num instead of i <= sqrt(num)
        # // to avoid repeatedly calling an expensive function sqrt().
        i = 2
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 1
        return True

    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        elif n == 2:
            return 0
        elif n == 3:
            return 1

        count = 2
        for i in range(5, n):
            if self.isPrime2(i):
                count += 1
        return count
    def countPrimes3(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])  #primes[i * i: n: i] = [False] * ((n-i*i - 1)//i + 1)

        return sum(primes)


so = Solution()
print(so.isPrime(25))
print(so.isPrime2(25))
print(so.countPrimes(1500000))
print(so.countPrimes3(1500000))
print(so.countPrimes(999983))
print(so.countPrimes(10000))  # 1229
print(so.countPrimes(10))  # 4
print(so.countPrimes(0))
print(so.countPrimes(1))
print(so.countPrimes(2))
print(so.countPrimes(3))
print(so.countPrimes(4))
print(so.countPrimes(5))

'''
Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0


'''
