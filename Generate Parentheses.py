'''

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

'''
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def generate(left, right, s):
            if left == 0 and right == 0:
                result.append(s)
            else:
                if left > 0:
                    generate(left - 1, right, s + "(")
                if right > 0 and left<right:
                    generate(left, right - 1, s + ")")

        generate(n, n, "")
        return result


def generateParenthesis2(self, n: int) -> List[str]:
    res = []
    stack = []

    def backtrack(openn, closen):

        if openn == closen == n:
            res.append("".join(stack))
            return

        if openn < n:
            stack.append('(')
            backtrack(openn + 1, closen)
            stack.pop()

        if openn > closen:
            stack.append(')')
            backtrack(openn, closen + 1)
            stack.pop()

    backtrack(0, 0)
    return res


so = Solution()
print(so.generateParenthesis(3))
'''

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
'''
