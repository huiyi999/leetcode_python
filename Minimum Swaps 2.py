import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = 0
    for i in range(len(arr)):
        while arr[i] != i + 1:
            t = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = t
            count += 1
    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input())
    #
    # arr = list(map(int, input().rstrip().split()))
    arr1 = [2, 3, 4, 1, 5]
    arr3 = [4, 3, 1, 2]
    arr2 = [1, 3, 5, 2, 4, 6, 7]
    res1 = minimumSwaps(arr1)
    print(res1)
    res2 = minimumSwaps(arr2)
    print(res2)

    # fptr.write(str(res) + '\n')
    #
    # fptr.close()

'''
Sample 1
Input: 2 3 4 1 5
Output 3
So, we need a minimum of  swaps to sort the array in ascending order.

Sample 2
Input: 1 3 5 2 4 6 7
Output: 3
So, we need a minimum of  swaps to sort the array in ascending order.
'''
