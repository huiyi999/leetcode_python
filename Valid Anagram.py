import collections
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t): return False
        counter = Counter(list(s))
        for char in t:
            counter[char] -= 1  # dict.get(key, default = None)
        # print(counter)
        return all(x == 0 for x in counter.values())
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c = collections.Counter(s)
        d = collections.Counter(t)

        return c == d

so = Solution()
so.isAnagram("anagram", "nagaram")
'''
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''
