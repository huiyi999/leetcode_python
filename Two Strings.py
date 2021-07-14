# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the twoStrings function below.
def twoStrings(s1, s2):
    flag = False
    for ch in list(s2):
        if ch in s1:
            flag = True
    if flag:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # q = int(input())
    #
    # for q_itr in range(q):
    #     s1 = input()
    #
    #     s2 = input()
    #
    #     result = twoStrings(s1, s2)
    #
    #     fptr.write(result + '\n')
    #
    # fptr.close()
    s11 = "hello"
    s21 = "world"

    s12 = "hi"
    s22 = "world"

    print(twoStrings(s11, s21))
    print(twoStrings(s12, s22))

'''
Sample Input
hello
world
Sample Output
YES

Sample Input
hi
world
Sample Output
NO



'''
