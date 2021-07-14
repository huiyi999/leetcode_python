from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        last = nums[0]
        length = len(nums)
        i = 1
        while 1:
            if i < length:
                if nums[i] == last:
                    nums.remove(nums[i])
                    length -= 1
                    continue
                else:
                    last = nums[i]
            else:
                break
            i += 1
        print(nums)
        return len(nums)

    def removeDuplicates2(self, nums: List[int]) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        print(nums)
        return i + 1


so = Solution()
print(so.removeDuplicates2([1, 1, 2]))
print(so.removeDuplicates2([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
'''
Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't matter what values are set beyond the returned length.

'''
