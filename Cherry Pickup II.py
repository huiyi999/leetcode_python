'''
Given a rows x cols matrix grid representing a field of cherries.
Each cell in grid represents the number of cherries that you can collect.

You have two robots that can collect cherries for you, Robot #1 is located at the top-left corner (0,0) ,
and Robot #2 is located at the top-right corner (0, cols-1) of the grid.

Return the maximum number of cherries collection using both robots  by following the rules below:

From a cell (i,j), robots can move to cell (i+1, j-1) , (i+1, j) or (i+1, j+1).
When any robot is passing through a cell, It picks it up all cherries, and the cell becomes an empty cell (0).
When both robots stay on the same cell, only one of them takes the cherries.
Both robots cannot move outside of the grid at any moment.
Both robots should reach the bottom row in the grid.

Constraints:
rows == grid.length
cols == grid[i].length
2 <= rows, cols <= 70
0 <= grid[i][j] <= 100
'''
from math import inf
from typing import List

'''
思路是动态规划。设f[i][j][k]表示当两个机器人走到了第 i 行，第一个机器人走到第 j 列，第二个走到第 k 列时，最大的路径数字和。则有递推关系

'''


class Solution:

    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[[-1 for _i in range(n)] for _j in range(n)] for _j in range(m)]
        print(len(dp), len(dp[0]), len(dp[0][0]))

        dp[0][0][n - 1] = grid[0][0] + grid[0][n - 1]

        for i in range(1, m):  # i represents ith row robots stand
            for j in range(0, min(i, n - 1) + 1):  # j represents jth column robot1 stands
                for k in range(max(0, n - i - 1), n):  # k represents kth column robot2 stands
                    for d1 in range(-1, 2):
                        for d2 in range(-1, 2):
                            idx1 = j + d1
                            idx2 = k + d2
                            # print("~~~~", idx1, idx2)
                            if 0 <= idx1 and idx1 < n and 0 <= idx2 and idx2 < n:
                                if dp[i - 1][idx1][idx2] != -1:
                                    if j == k:
                                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][idx1][idx2] + grid[i][j])
                                    else:
                                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][idx1][idx2] + grid[i][j] + grid[i][k])
        res = float('-inf')
        for i in range(n):
            res = max(res, max(dp[m - 1][i]))
        return res

    def cherryPickup2(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dp(row, c1, c2):
            if c1 < 0 or c1 >= n or c2 < 0 or c2 >= n:
                return -inf
            # current cell
            result = 0
            result += grid[row][c1]
            if c1 != c2:
                result += grid[row][c2]
            # transition
            if row != m - 1:
                result += max(dp(row + 1, nc1, nc2)
                              for nc1 in [c1, c1 + 1, c1 - 1]
                              for nc2 in [c2, c2 + 1, c2 - 1])
            return result

        return dp(0, 0, n - 1)


solution = Solution()
print(solution.cherryPickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))

'''
Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
Output: 24
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
Total of cherries: 12 + 12 = 24.


Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
Output: 28
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
Total of cherries: 17 + 11 = 28.
Example 3:

Input: grid = [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]
Output: 22
Example 4:

Input: grid = [[1,1],[1,1]]
Output: 4

'''
