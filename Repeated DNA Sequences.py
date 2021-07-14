'''
All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T',
for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Constraints:
0 <= s.length <= 105
s[i] is 'A', 'C', 'G', or 'T'.

'''
from typing import List


class Solution:
    '''
    approach 2
    '''

    def findRepeatedDnaSequences2(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        d = {}
        ans = []
        for i in range(len(s) - 9):
            key = s[i:i + 10]
            if key in d:
                d[key] += 1
                if d[key] == 2:
                    ans.append(key)
            else:
                d[key] = 1
        return ans

    '''
    appraoch 1
    '''

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = dict()
        for i in range(len(s) - 9):
            key = s[i:i + 10]
            if key not in result:
                result[key] = 1
            else:
                result[key] = result[key] + 1

        ans = []
        for (key, value) in result.items():
            if value > 1:
                ans.append(key)

        return ans


solution = Solution()
print(solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(solution.findRepeatedDnaSequences("AAAAAAAAAAAAA"))
'''
Example 1:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
'''
