'''
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
'''
import math


class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        flag = 1
        if x < 0:
            flag = 0
            x = 0 - x
        while x != 0:
            remainder = x % 10
            # print(remainder)
            num = num * 10 + remainder
            x //= 10
            # break
        if not flag:
            num = 0 - num
        if num > math.pow(2, 31) - 1 or num < -math.pow(2, 31):
            return 0
        return num

    def reverse2(self, x: int) -> int:
        if x > 0:
            result = int(str(x)[::-1])
        else:
            result = -int(str(abs(x))[::-1])
        if result > (2 ** 31 - 1) or result < -(2 ** 31):
            return 0
        else:
            return result


solution = Solution()

print(solution.reverse(123))
print(solution.reverse(-123))
print(solution.reverse(120))
print(solution.reverse(0))

sentence = "aWESOME is cODING"
words = sentence.split(" ")


def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    words = sentence.split(" ")
    words.reverse()
    for j in range(len(words)):
        temp = list(words[j])
        for i in range(len(temp)):
            if temp[i].isupper():
                temp[i] = temp[i].lower()
            else:
                temp[i] = temp[i].upper()
        words[j] = "".join(temp)

    return " ".join(words)


print(('o').isupper())
print(reverse_words_order_and_swap_cases("aWESOME is cODING"))


class Rectangle:

    def Rectangle(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


'''
Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0

'''
