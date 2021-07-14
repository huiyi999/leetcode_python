'''
Given a string s, find the length of the longest substring without repeating characters.
'''


class Solution:
    def lengthOfLongestSubstring3(self, s):
        """
        一次遍历时，使用字典保存每个字符第一次出现的位置。
        当right向后遍历的过程中，如果这个字符在字典中，说明这个字符在前面出现过，即这个区间已经不是题目要求的不含重复字符的区间了，因此，需要移动left。
        移动left到哪里呢？有个快速的方法，那就是移动到right字符在字典中出现的位置（即s[right]在前面的位置）的下一个位置。

        :type s: str
        :rtype: int
        """
        left, right = 0, 0
        chars = set()
        res = 0
        while left < len(s) and right < len(s):
            if s[right] in chars:
                if s[left] in chars:
                    chars.remove(s[left])
                left += 1
            else:
                chars.add(s[right])
                right += 1
                res = max(res, len(chars))
        return res

    def lengthOfLongestSubstring2(self, s):
        """使用双指针，[left, right]双闭区间来保存子串的左右区间，对应着这个区间我们维护一个set，这个set里面全部是不重复的字符。
        使用while循环，如果right字符不在set中，就让它进去；如果right在，就把left对应的字符给remove出去。
        所以，当我们得到一个right位置的字符时，通过移动left和修改[left,right]区间内对应的的set，来保持了一个最小的不重复字符区间。
        需要注意的是，移动left的次数不一定就是1次，因为我们要保证left和right之间没有重复字符，而新添加的right字符出现的位置不一定刚刚就是left指向的位置。
        :type s: str
        :rtype: int
        """
        left, right = 0, 0
        res = 0
        chars = dict()
        for right in range(len(s)):
            if s[right] in chars:
                left = max(left, chars[s[right]] + 1)
            chars[s[right]] = right
            res = max(res, right - left + 1)
        return res

r
so = Solution()
print(so.lengthOfLongestSubstring2("abcabcbb"))
print(so.lengthOfLongestSubstring2("bbbbb"))
print(so.lengthOfLongestSubstring2("pwwkew"))
print(so.lengthOfLongestSubstring2(""))
print(so.lengthOfLongestSubstring2("dvdf"))

'''
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0

'''
