'''
You are given an array of integers nums, there is a sliding window of size k
which is moving from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

Return the max sliding window.

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
'''
import collections
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:

        que = [(-1000000, 1000000)]
        ans = []
        for i in range(len(nums)):
            while len(que) > 0 and i - que[0][0] >= k:
                del que[0]
            while len(que) > 0 and que[-1][1] <= nums[i]:
                que.pop()
            que.append((i, nums[i]))
            if i >= k - 1:
                ans.append(que[0][1])
        return ans

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums) and k == 1: return nums[0]

        result = []
        q = deque()

        for i in range(len(nums)):
            # the first/left (max) element is out of the current window
            if q and i - q[0] == k:   # q 里面存的index满了，移除左边的
                q.popleft()

            while q:   # q 里面存的最后一个index 的num比当前num小，弹出
                # pop useles elements from last/right of the queue
                if nums[q[-1]] < nums[i]:
                    q.pop()
                else:
                    break

            q.append(i)

            if i >= k - 1:  # i == k-1 is the beginning of a full window，窗口满了之后，开始保存最值
                result.append(nums[q[0]])

        return result


'''
Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
Example 3:

Input: nums = [1,-1], k = 1
Output: [1,-1]
Example 4:

Input: nums = [9,11], k = 2
Output: [11]
Example 5:

Input: nums = [4,-2], k = 2
Output: [4]

'''
