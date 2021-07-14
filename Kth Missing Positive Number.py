'''
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length
'''
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        for num in range(1, 10001):
            if num in arr:
                continue
            else:
                count += 1
                if count == k:
                    return num
        return 0

    def findKthPositive2(self, arr: List[int], k: int) -> int:
        all = {i for i in range(1, k + len(arr) + 1, 1)}
        missing = (list(set(all) - set(arr)))
        missing.sort()
        return missing[k - 1]

    def findKthPositive3(self, arr: List[int], k: int) -> int:
        '''res = []
        for i in range(1, max(arr)):
            if not i in arr:
                res.append(i)

        if k <= len(res):
            return res[k-1]
        else:
            return len(arr) + k'''

        i, m, len_a = 0, 0, len(arr)
        while k > 0:
            m += 1
            if i < len(arr) and arr[i] == m:
                i += 1
            else:
                k -= 1
        return m


'''
Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

'''
