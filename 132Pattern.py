'''
Given an array of n integers nums, a 132 pattern is a subsequence of
three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?

Constraints:
n == nums.length
1 <= n <= 104
-109 <= nums[i] <= 109
'''

'''
题意很简单，就是在一串数字中按顺序找出三个数字(不需要相邻)s1, s2, s3，满足s1<s3<s2，
这个题目类似于另一个题目Increasing Triplet Subsequence(s1<s2<s3)，
那道题目限制了O(n) time, O(1) space，通过维护s1<s2，一旦发现了s2<s3就达到目的来实现。

此题类似，通过维护s2>s3，一旦发现s1<s3来实现，所以遍历数组的顺序采用从右向左，
维护s2>s3则通过一个栈和一个变量来实现，栈来表示s2，变量来表示s3。
当遍历到的第i个元素，若input[i]比s3大，就将input[i]入栈，入栈时要注意，
若input[i]大于栈顶，则将栈顶赋值给s3，直到input[i]不在大于栈顶，然后再将其入栈。
整个过程始终维护栈中的所有值都大于s3，当遍历到比s3小的值，直接返回true。
'''
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        stack = []
        s3 = float('-inf')
        # The num which is larger than the third and before third is stored in the 'stack'
        for num in reversed(nums):
            if num < s3: return True
            while stack and stack[-1] < num:   # 若num大于栈顶，则将栈顶赋值给s3，直到num不在大于栈顶，然后再将其入栈。
                s3 = stack.pop()
            stack.append(num)
        return False


solution = Solution()
print(solution.find132pattern([1, 2, 3, 4]))  # Output: false
print(solution.find132pattern([3, 1, 4, 2]))  # Output: true
print(solution.find132pattern([-1, 3, 2, 0]))  # Output: true
print(solution.find132pattern([-2, 1, 2, -2, 1, 2]))  # Output: true
print(solution.find132pattern([0, 1, 1, 0, 1, 0]))  # Output: false

'''
Example 1:
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Example 2:
Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:
Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
'''
