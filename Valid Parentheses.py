'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


'''


class Solution:
    def isValid4(self, s: str) -> bool:
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        open = []
        for c in s:
            if c in brackets:
                open.append(c)
            else:
                if not open:
                    return False
                elif c != brackets[open[-1]]:
                    return False
                elif c == brackets[open[-1]]:
                    open.pop(-1)
        return not open

    def isValid3(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pars = [None]
        parmap = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in parmap:
                if parmap[c] != pars.pop():
                    return False
            else:
                pars.append(c)
        return len(pars) == 1

    def isValid2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pars = [None]
        parmap = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in parmap and parmap[c] == pars[len(pars) - 1]:
                pars.pop()
            else:
                pars.append(c)
        return len(pars) == 1

    def isValid(self, s: str) -> bool:
        stack = []
        characters = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if ch not in characters:  # ch not in characters.keys  说明是左半部分
                stack.append(ch)
            else:
                if not stack:
                    return False
                elif characters[ch] != stack.pop():
                    return False
                else:
                    stack.pop()

        return len(stack) == 0


so = Solution()
print(so.isValid("()"))
print(so.isValid("()[]{}"))
print(so.isValid("(]"))
print(so.isValid("([)]"))
print(so.isValid("{[]}"))
'''
Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true

'''
