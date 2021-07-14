'''
Given a string s, remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
'''


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        visited = [0] * 27
        candidate = [0] * 27
        for c in s:
            # print(c)
            # print(ord(c)-ord('a'))  #python no directly character subtract
            candidate[ord(c) - ord('a')] = candidate[ord(c) - ord('a')] + 1

        stack = []

        for c in s:
            i = ord(c) - ord('a')
            candidate[i] = candidate[i] - 1
            if (visited[i]): continue
            while (len(stack) != 0 and c < stack[-1] and candidate[ord(stack[-1]) - ord('a')]):
                visited[ord(stack[-1]) - ord('a')] = 0
                stack.pop()

            stack.append(c)
            visited[i] = 1
        str1 = ""

        return ''.join(stack)

    def removeDuplicateLetters2(self, s: str) -> str:

        """
        cdadabcc

        01234567
        43131244

        1: 2, 4
        2: 5
        3: 1, 3
        4: 0, 6, 7

        stack = []
        c d
        a d b c

        """

        last_index = {}

        for i, char in enumerate(s):
            last_index[char] = i

        stack = []
        used = set()

        i = 0
        while i < len(s):
            curr_char = s[i]
            if curr_char not in used:
                while stack and stack[-1] > curr_char and i < last_index[stack[-1]]:
                    used.discard(stack.pop())
                used.add(curr_char)
                stack.append(curr_char)
            i += 1

        return ''.join(stack)

    def removeDuplicateLetters3(self, s: str) -> str:
        ht = {}
        for i, c in enumerate(s):
            ht[c] = i
        stack = []
        for i, c in enumerate(s):
            if c in stack:
                continue
            while stack and c < stack[-1] and ht[stack[-1]] > i:
                stack.pop()
            stack.append(c)
            # print(c, stack)
        return ''.join(stack)


'''
Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"

'''
