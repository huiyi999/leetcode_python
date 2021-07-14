'''
Given a string s and an integer k,
return the length of the longest substring of s
such that the frequency of each character in this substring is greater than or equal to k.

Constraints:
1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105
'''


'''
首先出现小于k次的字符一定不会出现在要求的子串中，
因此统计字符串中每个字符出现的次数，以小于k次的字符为分割点，将字符串分割为几个小片段。

对每个小片段，我们仍需要判断它是否满足每个字符出现次数不小于k，
所以对每个小片段递归分割。

终止条件是片段中每个字符次数都不小于k时返回片段长度。
'''

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)




'''
Example 1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

'''