# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    count = 0
    l = len(q)
    for i in range(l - 1, -1, -1):
        print("q: ",q)
        if q[i] != i + 1:
            if i - 1 >= 0 and q[i - 1] == i + 1:
                count += 1
                q[i - 1], q[i] = q[i], q[i - 1]

            elif i - 2 >= 0 and q[i - 2] == i + 1:
                count += 2
                q[i - 2]= q[i - 1]
                q[i - 1]=q[i]
                q[i]=i+1
            else:
                print("Too chaotic.")
                return
    print(count)


if __name__ == '__main__':
    # t = int(input())
    #
    # for t_itr in range(t):
    #     n = int(input())
    #
    #     q = list(map(int, input().rstrip().split()))
    test1 = [1, 2, 5, 3, 4, 7, 8, 6]
    test2 = [1, 2, 5, 3, 7, 8, 6, 4]
    minimumBribes(test1)  #4
    minimumBribes(test2)  #7

'''
Sample Input
STDIN       Function
-----       --------
2           t = 2
5           n = 5
2 1 5 3 4   q = [2, 1, 5, 3, 4]
5           n = 5
2 5 1 3 4   q = [2, 5, 1, 3, 4]
Sample Output
3
Too chaotic


'''
