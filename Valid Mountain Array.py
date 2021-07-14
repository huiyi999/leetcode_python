'''
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < A[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Constraints:
1 <= arr.length <= 104
0 <= arr[i] <= 104
'''
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        # peek = max(arr)
        peek = float("-inf")
        # print(peek)
        index = 0
        for i, num in enumerate(arr):
            if num > peek:
                peek = num
                index = i
            elif num == peek:
                return False
            else:
                break

        # print(index)
        if index == len(arr) - 1 or index == 0:
            return False

        for num in arr[index + 1:]:
            if num >= peek:
                return False
            else:
                peek = num

        return True

    def validMountainArray2(self, A: List[int]) -> bool:
        n = len(A)
        if n < 3: return False
        inc = A[0] < A[1]
        k = 0
        for i in range(1, n):
            if inc and A[i - 1] >= A[i]:
                k += 1
                inc = False
            if not inc and A[i - 1] <= A[i]:
                return False
        return k == 1


solution = Solution()
print(solution.validMountainArray([0, 3, 2, 1]))
print(solution.validMountainArray([2, 1]))
print(solution.validMountainArray([3, 5, 5]))
print(solution.validMountainArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

'''
Example 1:
Input: arr = [2,1]
Output: false

Example 2:
Input: arr = [3,5,5]
Output: false

Example 3:
Input: arr = [0,3,2,1]
Output: true

'''
