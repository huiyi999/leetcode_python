import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        print()
        return n > 0 and (3 ** 19) % n == 0  # 3^19=1162261467是小于2^31最大的3的倍数

    def isPowerOfThree2(self, n: int) -> bool:
        if n < 1:
            return False

        while n % 3 == 0:
            n /= 3

        return n == 1

    def isPowerOfThree3(self, n: int) -> bool:
        if n < 1: return False
        print(math.log10(n) / math.log10(3))
        print(5.1 % 1)
        print(math.log10(n) / math.log10(3) % 1)
        return math.log10(n) / math.log10(3) % 1 == 0


so = Solution()
print(so.isPowerOfThree3(45))
