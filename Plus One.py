from typing import List


class Solution:
    def plusOne3(self, digits: List[int]) -> List[int]:
        n = len(digits)
        flag = 0
        n = n - 1
        while n >= 0:
            if digits[n] < 9:
                digits[n] = digits[n] + 1
                flag = 1
                return digits
            else:
                digits[n] = 0
            n = n - 1
        if flag == 0:
            digits.insert(0, 1)
            return digits

    def plusOne2(self, digits: List[int]) -> List[int]:

        num_str = ''.join(str(digit) for digit in digits)
        answer = int(num_str) + 1

        if answer == 1 and len(num_str) > 1:
            digits[-1] = 1
            return digits

        return [int(x) for x in str(answer)]

    def plusOne(self, digits: List[int]) -> List[int]:
        reverse = [digits[i] for i in range(len(digits) - 1, -1, -1)]
        # print(reverse)
        flag = 0
        for i in range(len(digits)):
            if reverse[i] != 9:
                reverse[i] += 1
                flag = 0
                break
            else:
                reverse[i] = 0
                flag = 1
        if flag:
            reverse.append(1)
        digits = [reverse[i] for i in range(len(reverse) - 1, -1, -1)]
        # print(digits)
        return digits


so = Solution()
print(so.plusOne([1, 2, 3]))
print(so.plusOne([9, 9]))
print(so.plusOne([8, 9]))
print(so.plusOne([4, 3, 2, 1]))
print(so.plusOne([0]))

'''
Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Example 3:
Input: digits = [0]
Output: [1]


'''
