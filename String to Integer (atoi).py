class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. Read in and ignore any leading whitespace
        s = s.lstrip()

        if not s: return 0

        sign, number = "+", ''
        # 2. Check if the next character (if not already at the end of the string) is '-' or '+'

        if s[0] == "-" or s[0] == "+":
            sign = s[0]
            s = s[1:]

        # 3. Read in next the characters until the next non-digit charcter or the end of the input is reached.

        for x in s:
            if x.isdigit():
                number += x
            else:
                break

        # 4. Convert these digits into an integer
        # 5. If the integer is out of the 32-bit signed integer range
        if number == '':
            number = 0
        else:
            number = int(sign + number)
            if number > 2 ** 31 - 1:
                number = 2 ** 31 - 1
            elif number < -2 ** 31:
                number = -2 ** 31

        return number


so = Solution()
print(so.myAtoi("42"))
print(so.myAtoi("   -42"))
print(so.myAtoi("4193 with words"))
print(so.myAtoi("words and 987"))
print(so.myAtoi("-91283472332"))
print(so.myAtoi("+1"))
print(so.myAtoi("   +0 123"))

'''
Example 1:

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
Example 2:

Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.
Example 3:

Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.
Example 4:

Input: s = "words and 987"
Output: 0
Explanation:
Step 1: "words and 987" (no characters read because there is no leading whitespace)
         ^
Step 2: "words and 987" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "words and 987" (reading stops immediately because there is a non-digit 'w')
         ^
The parsed integer is 0 because no digits were read.
Since 0 is in the range [-231, 231 - 1], the final result is 0.
Example 5:

Input: s = "-91283472332"
Output: -2147483648
Explanation:
Step 1: "-91283472332" (no characters read because there is no leading whitespace)
         ^
Step 2: "-91283472332" ('-' is read, so the result should be negative)
          ^
Step 3: "-91283472332" ("91283472332" is read in)
                     ^
The parsed integer is -91283472332.
Since -91283472332 is less than the lower bound of the range [-231, 231 - 1], the final result is clamped to -231 = -2147483648.


'''
