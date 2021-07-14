# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_dict = {}
    for word in magazine:
        if word not in magazine_dict:
            magazine_dict[word] = 1
        else:
            magazine_dict[word] += 1
    print(magazine_dict)


    for word in note:
        if word not in magazine_dict:
            print("No")
            return
        elif magazine_dict[word]==0:
            print("No")
            return
        else:
            magazine_dict[word] -= 1
    print("Yes")


if __name__ == '__main__':
    # mn = input().split()
    #
    # m = int(mn[0])
    #
    # n = int(mn[1])
    #
    # magazine = input().rstrip().split()
    #
    # note = input().rstrip().split()
    # checkMagazine(magazine, note)
    m1 = "give me one grand today night".rstrip().split()
    n1 = "give one grand today".rstrip().split()
    m2 = "two times three is not four".rstrip().split()
    n2 = "two times two is four".rstrip().split()
    m3 = "ive got a lovely bunch of coconuts".rstrip().split()
    n3 = "ive got some coconuts".rstrip().split()
    checkMagazine(m1, n1)
    checkMagazine(m2, n2)
    checkMagazine(m3, n3)

''''
Sample Input:
6 4
give me one grand today night
give one grand today
Sample Output: Yes

Sample Input:
6 5
two times three is not four
two times two is four
Sample Output: No

Sample Input:
7 4
ive got a lovely bunch of coconuts
ive got some coconuts
Sample Output: No
'''
