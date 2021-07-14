'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Constraints:1 <= n <= 20
'''
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        visited = [[0] * n for _ in range(n)]
        matrix = [[0] * n for _ in range(n)]

        self.col, self.row = 0, 0
        self.curr = 1

        def spiral():
            move = False
            while self.col < n and not visited[self.row][self.col]:
                matrix[self.row][self.col] = self.curr
                self.curr += 1
                visited[self.row][self.col] = 1

                self.col += 1
                move = True

            self.row += 1
            self.col-=1
            print("right")
            print(matrix)
            print(self.col)
            while self.row < n and not visited[self.row][self.col]:
                matrix[self.row][self.col] = self.curr
                self.curr += 1
                visited[self.row][self.col] = 1

                self.row += 1
                move = True

            self.col -= 1
            self.row -= 1
            print("down")
            print(matrix)
            print(self.row)
            print(self.col)
            while self.col >= 0 and not visited[self.row][self.col]:
                matrix[self.row][self.col] = self.curr
                self.curr += 1
                visited[self.row][self.col] = 1

                self.col -= 1
                move = True
            print("right")
            print(matrix)
            print(self.row)
            print(self.col)
            self.col += 1
            self.row -= 1

            while self.row >=0 and not visited[self.row][self.col]:
                matrix[self.row][self.col] = self.curr
                self.curr += 1
                visited[self.row][self.col] = 1

                self.row -= 1
                move = True
            self.row += 1
            self.col += 1
            print(matrix)
            if move:
                spiral()

        spiral()
        return matrix


solution = Solution()
print(solution.generateMatrix(3))
'''
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Input: n = 1
Output: [[1]]

'''
