'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.
Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        # print(intervals)
        result = []
        start, end = intervals[0][0], intervals[0][1]
        for interval in intervals[1:]:
            # print(interval)
            if interval[0] > end:
                result.append([start, end])
                start, end = interval[0], interval[1]

            else:
                end = max(interval[1], end)
        result.append([start, end])
        return result


solution = Solution()
print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(solution.merge([[1, 4], [4, 5]]))
print(solution.merge([[1, 4], [0, 4]]))

'''
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

'''
