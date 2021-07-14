from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        # print(nums1)
        nums2.sort()

        point1, point2 = 0, 0
        res = []

        while point1 < len(nums1) and point2 < len(nums2):
            if nums1[point1] == nums2[point2]:
                res.append(nums1[point1])
                point1 += 1
                point2 += 1
            elif nums1[point1] > nums2[point2]:
                point2 += 1
            else:
                point1 += 1
        # print(res)
        return res

    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts1 = Counter(nums1)
        print(counts1)
        intersection = []
        for num in nums2:
            if counts1[num] > 0:
                intersection.append(num)
                counts1[num] -= 1
        return intersection


solution = Solution()
solution.intersect([1, 2, 2, 1], [2, 2])
solution.intersect([4, 9, 5], [9, 4, 9, 8, 4])
solution.intersect2([1, 2, 2, 1], [2, 2])
solution.intersect2([4, 9, 5], [9, 4, 9, 8, 4])
'''
Example 1:

Input: nums1 = [1,2,2,1], nums2 =  [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]


'''
