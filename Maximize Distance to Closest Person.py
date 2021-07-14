'''
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat,
and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

Return that maximum distance to the closest person.

Constraints:
2 <= seats.length <= 2 * 104
seats[i] is 0 or 1.
At least one seat is empty.
At least one seat is occupied.
'''
from typing import List


class Solution:
    def maxDistToClosest2(self, seats: List[int]) -> int:
        s_range = [i for i, o in enumerate(seats) if o]  # store the index of occupied

        max_d = s_range[0]

        for i, j in zip(s_range, s_range[1:]):
            print(i,j)
            max_d = max(max_d, (j - i) // 2)
            print(max_d)

        if s_range[-1] < len(seats) - 1:
            max_d = max(max_d, len(seats) - s_range[-1] - 1)

        return max_d

    def maxDistToClosest(self, seats: List[int]) -> int:
        '''
        这是一个系列题目，都是从左向右遍历一遍，从右向左遍历一遍。
        对于每一个位置，都求其左边距离其最近的1和其右边距离其最近的1与其的距离，保留两者这之间较小的值，
        就代表这个位置的“安全距离”，最终返回所有的位置距离中最大的值即可。
        '''
        pre = float('-inf')
        result = []
        for i in range(len(seats)):
            if seats[i] == 1:
                pre = i
            result.append(i - pre)

        pre = float('inf')
        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 1:
                pre = i
            if seats[i] == 1:
                pre = i
            result[i] = min(result[i], pre - i)
        return max(result)

solution=Solution()
solution.maxDistToClosest2([1,0,0,0,1,0,1])


'''
Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.

Example 2:
Input: seats = [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.

Example 3:
Input: seats = [0,1]
Output: 1
'''
