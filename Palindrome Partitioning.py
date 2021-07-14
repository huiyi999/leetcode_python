'''
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.


list[<start>:<stop>:<step>]
a[::-1], it starts from the end towards the first taking each element
'''
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if len(s) == 0:
            res.append(path)

        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[0:i]):
                self.dfs(s[i:], path + [s[0:i]], res)
                # path.pop()

    def isPalindrome(self, s):
        # if len(s) == 0:
        #     return False
        # else:
        #     start = 0
        #     end = len(s) - 1
        #     while start <= end:
        #         if s[start] != s[end]:
        #             return False
        #         else:
        #             start += 1
        #             end -= 1
        # return True
        if len(s) == 0:
            return False
        else:
            if s == s[::-1]:
                return True
        return False


solution = Solution()
print(solution.partition("aab"))

print(solution.isPalindrome("aabc"))
print(solution.isPalindrome("abba"))
print(solution.isPalindrome("aba"))

'''
Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

'''
