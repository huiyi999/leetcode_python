# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/886/
'''

 1.     1
 2.     11
 3.     21
 4.     1211
 5.     111221
 6.     312211
 7.     13112221
 8.     1113213211
 9.     31131211131221
10.     13211311123113112211

'''
from collections import Counter


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = self.countAndSay(n - 1) + "*"
        count = 1
        res = ""
        for j in range(1, len(s)):
            if s[j] == s[j - 1]:
                count += 1
            else:
                res += str(count) + s[j - 1]
                count = 1
        return res

    def countAndSay2(self, n: int) -> str:

        if n == 1:
            return '1'

        mylist = list(self.countAndSay(n - 1))
        mystr = ''
        count = 0
        curr = mylist[0]

        for i in mylist:

            if i == curr:
                count += 1

            else:
                mystr += str(count) + str(curr)
                count = 1
                curr = i

        mystr += str(count) + str(curr)
        return mystr


so = Solution()
print(so.countAndSay(1))
print(so.countAndSay(2))
print(so.countAndSay(4))
print(so.countAndSay(10))
print(so.countAndSay(7))

'''
Example 1:
Input: n = 1
Output: "1"
Explanation: This is the base case.

Example 2:
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
'''
