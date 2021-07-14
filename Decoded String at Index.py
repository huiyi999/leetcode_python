'''
An encoded string S is given.  To find and write the decoded string to a tape,
the encoded string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more times in total.
Now for some encoded string S, and an index K, find and return the K-th letter (1 indexed) in the decoded string.

Constraints:
2 <= S.length <= 100
S will only contain lowercase letters and digits 2 through 9.
S starts with a letter.
1 <= K <= 10^9
It's guaranteed that K is less than or equal to the length of the decoded string.
The decoded string is guaranteed to have less than 2^63 letters.
'''



'''
比如，对于一个解码了的字符串，appleappleappleappleappleapple，并且要求的索引K=24的话，那么结果和K=4是一样的。
因为单词apple的size=5，重复了6次。所以第K个索引和第K%size个索引是一样的。

所以我们使用反向的计算，保持追踪解码字符串的size，如果解码字符串等于一个word重复了d次的时候，我们可以把K变化为K % (word.length)
'''

class Solution:
    # def decodeAtIndex(self, S: str, K: int) -> str:
    #     tempStr = ''
    #     for char in S:
    #         if char.isdigit():
    #             tempNum = char
    #             tempStr = int(tempNum) * tempStr
    #             if len(tempStr) > K:
    #                 return tempStr[K - 1]
    #         elif char.isalpha():
    #             tempStr += char
    #     # print(tempStr)
    #
    #     return tempStr[K - 1]
    def decodeAtIndex(self, S: str, K: int) -> str:
        size = 0
        for c in S:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1
        print(size)
        for c in reversed(S):
            print(c)
            K %= size
            if K == 0 and c.isalpha():
                return c
            if c.isdigit():
                size /= int(c)
                print(size)
            else:
                size -= 1


solution = Solution()
print(solution.decodeAtIndex("leet2code3", 10))
print(solution.decodeAtIndex("ha22", 5))
print(solution.decodeAtIndex("a2345678999999999999999", 1))
print(solution.decodeAtIndex("abc", 1))
'''
Example 1:

Input: S = "leet2code3", K = 10
Output: "o"
Explanation: 
The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".
Example 2:

Input: S = "ha22", K = 5
Output: "h"
Explanation: 
The decoded string is "hahahaha".  The 5th letter is "h".
Example 3:

Input: S = "a2345678999999999999999", K = 1
Output: "a"
Explanation: 
The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".


"cpmxv8ewnfk3xxcilcmm68d2ygc88daomywc3imncfjgtwj8nrxjtwhiem5nzqnicxzo248g52y72v3yujqpvqcssrofd99lkovg"
480551547

Time Limit Exceeded
'''
