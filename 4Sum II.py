'''
Given four lists A, B, C, D of integer values,
compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500.
All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.


'''
import collections
from typing import List


class Solution:

    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB = collections.Counter(a + b for a in A for b in B)
        return sum(AB[-c - d] for c in C for d in D)


# def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
#     '''
#      Time Limit Exceeded
#     '''
#     n = len(A)
#     res = 0
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 for l in range(n):
#                     if A[i] + B[j] + C[k] + D[l] == 0:
#                         res += 1
#     return res

'''
A Counter is a dict subclass for counting hashable objects. 
It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. 
Counts are allowed to be any integer value including zero or negative counts. 
The Counter class is similar to bags or multisets in other languages.
'''

'''
Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

'''
