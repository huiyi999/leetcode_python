'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces .
The integer division should truncate toward zero.

之前的运算符是+，那么需要把之前的数字num进栈，然后等待下一个操作数的到来。
之前的运算符是-，那么需要把之前的数字求反-num进栈，然后等待下一个操作数的到来。
之前的运算符是×，那么需要立刻出栈和之前的数字相乘，重新进栈，然后等待下一个操作数的到来。
之前的运算符是/，那么需要立刻出栈和之前的数字相除，重新进栈，然后等待下一个操作数的到来。
'''
import re


class Solution:
    def calculate2(self, s: str) -> int:

        num = re.split("[+-/*]", s)
        num = list(map(int, num))

        res = 0
        i = 1
        operater = []

        while i < len(s):
            if s[i] in '+/*-':
                operater.append(s[i])
            i += 1

        if not operater:
            return num[0]
        calculated = [False] * len(operater)
        visited = [False] * len(num)

        for i in range(len(operater)):
            if operater[i] == '*' and not calculated[i]:
                if not visited[i] and not visited[i + 1]:
                    res += num[i] * num[i + 1]
                    visited[i] = True
                    visited[i + 1] = True
                elif not visited[i] and visited[i + 1]:
                    res = num[i] * res
                    visited[i] = True
                elif visited[i] and not visited[i + 1]:
                    res = res * num[i + 1]
                    visited[i + 1] = True
                calculated[i] = True

            if operater[i] == '/' and not calculated[i]:
                if not visited[i] and not visited[i + 1] and num[i + 1] != 0:
                    res += num[i] // num[i + 1]
                    visited[i] = True
                    visited[i + 1] = True
                elif not visited[i] and visited[i + 1] and res != 0:
                    res = num[i] // res
                    visited[i] = True
                elif visited[i] and not visited[i + 1] and num[i + 1] != 0:
                    res = res // num[i + 1]
                    visited[i + 1] = True
                calculated[i] = True
        for i in range(len(operater)):
            if operater[i] == '+' and not calculated[i]:

                if not visited[i] and not visited[i + 1]:
                    res += num[i] + num[i + 1]
                    visited[i] = True
                    visited[i + 1] = True
                elif not visited[i] and visited[i + 1]:
                    res = num[i] + res
                    visited[i] = True

                elif visited[i] and not visited[i + 1]:
                    res = res + num[i + 1]
                    visited[i + 1] = True
                calculated[i] = True
            elif operater[i] == '-' and not calculated[i]:
                if not visited[i] and not visited[i + 1]:
                    res += num[i] - num[i + 1]
                    visited[i] = True
                    visited[i + 1] = True
                elif not visited[i] and visited[i + 1]:
                    res = num[i] - res
                    visited[i] = True
                elif visited[i] and not visited[i + 1]:
                    res = res - num[i + 1]
                    visited[i + 1] = True
                calculated[i] = True

        return res

    def calculate(self, s):

        stack = []
        pre_op = '+'
        num = 0
        for i, each in enumerate(s):
            if each.isdigit():
                num = 10 * num + int(each)
            if i == len(s) - 1 or each in '+-*/':
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    stack.append(stack.pop() * num)
                elif pre_op == '/':
                    top = stack.pop()
                    if top < 0:
                        stack.append(int(top / num))
                    else:
                        stack.append(top // num)
                pre_op = each
                num = 0
        return sum(stack)


solution = Solution()
print(solution.calculate("3+2*2"))
print(solution.calculate(" 3/2 "))
print(solution.calculate(" 3+5 / 2 "))
print(solution.calculate("1*2+3*4"))  #14
print(solution.calculate("1"))  #1
print(solution.calculate("1*2-3/4+5*6-7*8+9/10"))  #-24
'''
Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5



'''
