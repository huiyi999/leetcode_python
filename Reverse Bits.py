'''
Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
Follow up:

If this function is called many times, how would you optimize it?

Constraints:
The input must be a binary string of length 32
'''
import math


class Solution:
    def reverseBits2(self, n: int) -> int:
        res = 0
        print(bin(n))
        print(n & 1)
        for i in range(32):
            res = (res << 1) + (n & 1)
            # print(res)
            n = n >> 1
            # print(n)
        return res

    def reverseBits(self, n: int) -> int:
        n_bit = bin(n).replace("0b", "").zfill(32)
        # n_bit_reverse=n_bit[::-1]
        # print(n_bit)
        # print(n_bit_reverse)

        return int(n_bit[::-1], 2)

    def reverseBits3(self, n: int) -> int:
        n_bit = bin(n).replace("0b", "")

        ans = 0
        bits = 32
        for i in range(len(n_bit) - 1, -1, -1):
            bits -= 1
            if n_bit[i] == "1":
                ans += math.pow(2, bits)
        return int(ans)


so = Solution()
print(so.reverseBits(10))
print(so.reverseBits2(10))
print(so.reverseBits3(10))
'''

Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
'''
