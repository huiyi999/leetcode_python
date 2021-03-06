'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.
For example, there won't be input like 3a or 2[4].

Constraints:
1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
'''


class Solution:
    def decodeString2(self, s: str) -> str:
        stack = []
        tempNum = ''
        tempStr = ''
        for char in s:
            if char.isdigit():
                tempNum += char
            elif char.isalpha():
                tempStr += char
            elif char == '[':
                stack.append(tempStr)
                stack.append(int(tempNum))
                tempNum = ''
                tempStr = ''
            else:
                num = stack.pop()
                prevStr = stack.pop()
                tempStr = prevStr + num * tempStr
        return tempStr

    def decodeString(self, s: str) -> str:
        res = []
        nums = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = 0

                while i >= 0 and s[i].isdigit():
                    num = 10 * num + int(s[i])
                    i += 1

                nums.append(num)
            elif s[i] == '[' or s[i].isalpha():
                res.append(s[i])
                i += 1
            else:
                ch = res.pop()
                tmp = ""
                while ch != '[':
                    tmp = ch + tmp
                    ch = res.pop()
                num = nums.pop()
                new_char = num * tmp
                res.append(new_char)
                i += 1

        return "".join(res)


solution = Solution()
solution.decodeString("3[a]2[bc]")
solution.decodeString("3[a2[c]]")
solution.decodeString("2[abc]3[cd]ef")
solution.decodeString("abc3[cd]xyz")
solution.decodeString("100[leetcode]")

'''
Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Example 4:
Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
'''
