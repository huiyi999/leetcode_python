'''
Given a sorted (in ascending order) integer array nums of n elements and a target value,
write a function to search target in nums. If target exists, then return its index, otherwise return -1.

Note:

You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].
'''
from typing import List

'''
self代表的是类的实例。而self.__class__则指向类
在描述符类中，self指的是描述符类的实例
在继承时，传入的是哪个实例，就是那个传入的实例，而不是指定义了self的类的实例。


'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        print(target)
        low = 0
        high = len(nums) - 1
        mid = 0
        while high >= low:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1


solution = Solution()
nums1 = [-1, 0, 3, 5, 9, 12]
target1 = 9
print(solution.search(nums1, target1))

nums2 = [-1, 0, 3, 5, 9, 12]
target2 = 2
print(solution.search(nums2, target2))

# Example 1:
#
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
#
# Example 2:
#
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
