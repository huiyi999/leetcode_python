# !/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
from collections import Counter


def sherlockAndAnagrams(s):
    print(s)
    print(sorted(s))   # become a list
    count = Counter(
        ("".join(sorted(s[j:j + i]))   # sorts the character of substring and then join into a string
         for i in range(1, len(s))  # means the length of substring
         for j in range(0, len(s) - i + 1)))  #means the indice
    print(count)
    return sum(sum(range(i)) for i in count.values())
    # n = len(s)
    # res = 0
    # for l in range(1, n):
    #     cnt = {}
    #     for i in range(n - l + 1):
    #         subs = list(s[i:i + l])
    #         subs.sort()
    #         subs = ''.join(subs)
    #         if subs in cnt:
    #             cnt[subs] += 1
    #         else:
    #             cnt[subs] = 1
    #             res += cnt[subs] - 1
    # print(res)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # q = int(input())
    #
    # for q_itr in range(q):
    #     s = input()
    #
    #     result = sherlockAndAnagrams(s)
    #
    #     fptr.write(str(result) + '\n')
    #
    # fptr.close()
    s1 = "abba"
    s2 = "abcd"
    s3 = "ifailuhkqq"
    s4 = "kkkk"
    s5 = "cdcd"
    print(sherlockAndAnagrams(s1))
    print(sherlockAndAnagrams(s2))
    print(sherlockAndAnagrams(s3))
    print(sherlockAndAnagrams(s4))
    print(sherlockAndAnagrams(s5))

'''
Sample Input 0
2
abba
abcd
Sample Output 0
4
0


Sample Input 1
2
ifailuhkqq
kkkk
Sample Output 1
3
10


Sample Input 2
1
cdcd
Sample Output 2
5

'''
