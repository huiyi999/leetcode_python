'''

Given a column title as appear in an Excel sheet, return its corresponding column number.



'''
import math
import string


class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        n = 0
        for i in range(len(s) - 1, -1, -1):  # for i in s[::-1]:
            result += (ord(s[i]) - ord('A') + 1) * 26 ** n
            n += 1
        return int(result)

    def titleToNumber2(self, s: str) -> int:
        s = s.lower()
        place = 0
        res = 0
        for i in s[::-1]:
            res += (string.ascii_lowercase.index(i) + 1) * 26 ** place
            place += 1
        return res

    def titleToNumber3(self, s: str) -> int:
        t = s[-1]
        return ord(t) - 64 if len(s) == 1 else self.titleToNumber(s[0:-1]) * 26 + ord(t) - 64


print(ord('B') - ord('A') + 1)
so = Solution()
print(so.titleToNumber("A"))
print(so.titleToNumber("AB"))
print(so.titleToNumber("ZY"))
'''
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
'''
