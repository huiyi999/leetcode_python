#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findSum' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. 2D_INTEGER_ARRAY queries
#

def findSum(numbers, queries):
    # Write your code here
    ans = []
    for j in range(len(queries)):
        res = sum(numbers[queries[j][0] - 1:queries[j][1]]) + queries[j][2] * numbers[
                                                                              queries[j][0] - 1:queries[j][1]].count(0)
        ans.append(res)
    print(ans)
    return ans


findSum([20, 30, 0, 10], [[1, 3, 10]])
findSum([5, 10, 10], [[1, 2, 5]])
findSum([-5, 0], [[2, 2, 20], [1, 2, 10]])

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     numbers_count = int(input().strip())
#
#     numbers = []
#
#     for _ in range(numbers_count):
#         numbers_item = int(input().strip())
#         numbers.append(numbers_item)
#
#     queries_rows = int(input().strip())
#     queries_columns = int(input().strip())
#
#     queries = []
#
#     for _ in range(queries_rows):
#         queries.append(list(map(int, input().rstrip().split())))
#
#     result = findSum(numbers, queries)
#
#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')
#
#     fptr.close()
