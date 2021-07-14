'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
'''


class Solution:
    '''
    appraoch 1: 库函数: 96 ms
    库函数都是针对一维数组的查找，把给出的数组变成一维的。在numpy中有reshape函数
    '''

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        import numpy as np
        matrix = np.reshape(matrix, [1, -1])
        return target in matrix

    '''
    approach 2:
    '''

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        tmp = []
        for row in matrix:
            if row[-1] == target:
                return True
            elif row[-1] > target:
                tmp = row
                break
        if not tmp:
            return False
        else:
            return target in tmp

        # left = 0
        # right = len(tmp)
        # while left < right:
        #     mid = (left + right) // 2
        #     if tmp[mid] > target:
        #         left = mid
        #     elif tmp[mid] < target:
        #         right = mid
        #     else:
        #         return True
        # return False


'''
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false

Input: matrix = [], target = 0
Output: false
'''
