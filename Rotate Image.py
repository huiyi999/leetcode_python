from typing import List

'''
规律：
旋转90°即：A[0,0] 转到 A[0,n] 位置；A[0,n] 转到 A[n,n] 位置；A[n,n] 转到 A[n,0] 位置；A[n,0] 转到 A[0,0] 位置。然后依次类推
上一步操作的是最外层的一层 环，我们只需要一层层往里执行相同的操作，最终即可完成整个矩阵的旋转
假设矩阵是 n*n 的，那么我们对 n/2 个环执行旋转即可完成
对于任一层的环，假如起始索引为 start，终止索引为 end，那么左上右下四个点分别可有表示为：A[start][start]，A[start][end]，A[end][start]，A[end][end]
某层环内的循环规律即 A[start][start->end]，A[start->end][end]，A[end][end->start]，A[end->start][start]。箭头表示递变情况
'''


'''
first reverse, then transpose

'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix) // 2):
            start = i
            end = len(matrix) - i - 1
            for j in range(0, end - start):
                tmp = matrix[start][start + j]
                matrix[start][start + j] = matrix[end - j][start]
                matrix[end - j][start] = matrix[end][end - j]
                matrix[end][end - j] = matrix[start + j][end]
                matrix[start + j][end] = tmp

    def rotate2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose
        n = len(matrix)
        for i in range(0, n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reverse each row
        for i in range(0, n):
            row = matrix[i]
            for j in range(0, n // 2):
                row[j], row[n - 1 - j] = row[n - 1 - j], row[j]

    def rotate3(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # reverse
        matrix.reverse()
        print(matrix)
        # transpose
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


so = Solution()
so.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
so.rotate3([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

'''
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Example 3:
Input: matrix = [[1]]
Output: [[1]]

Example 4:
Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]
'''
