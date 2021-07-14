'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2^31.


'''


class Solution:
    def hammingDistance2(self, x: int, y: int) -> int:
        ans = 0
        diff = x^y
        while diff:
            ans += 1
            diff = diff&(diff-1)
        return ans
    def hammingDistance(self, x: int, y: int) -> int:

        print(x ^ y, bin(x ^ y), bin(x ^ y).count("1"))
        return bin(x ^ y).count("1")


so = Solution()
print(so.hammingDistance(1, 4))
print(so.hammingDistance(93, 73))
'''
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

'''
