from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m,len(nums1)):
            nums1[i]=nums2[i-m]
        nums1.sort()


    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        del nums1[m:]
        del nums2[n:]

        i = 0
        while i < len(nums1) and len(nums2) > 0:
            if nums2[0] < nums1[i]:
                nums1.insert(i, nums2.pop(0))
                continue

            i += 1

        if len(nums2) > 0:
            nums1 += nums2

        return




'''


Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
'''