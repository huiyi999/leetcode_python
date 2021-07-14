'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

'''
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            tmp = [0 for _ in range(i + 1)]
            tmp[0], tmp[-1] = 1, 1
            for j in range(1, i):
                tmp[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(tmp)
        for i in range(numRows):
            print(triangle[i])
        return triangle


so = Solution()
print(so.generate(5))
print(so.generate(1))
print(so.generate(15))

'''

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
'''
