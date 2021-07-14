'''
There are some spherical balloons spread in two-dimensional space.
For each balloon, provided input is the start and end coordinates of the horizontal diameter.
Since it's horizontal, y-coordinates don't matter, and hence the x-coordinates of start and end of the diameter suffice.
The start is always smaller than the end.

An arrow can be shot up exactly vertically from different points along the x-axis.
A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend.
There is no limit to the number of arrows that can be shot. An arrow once shot keeps traveling up infinitely.

Given an array points where points[i] = [xstart, xend],
return the minimum number of arrows that must be shot to burst all balloons.
Constraints:

0 <= points.length <= 104
points.length == 2
-231 <= xstart < xend <= 231 - 1

'''


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) <= 1: return len(points)
        points.sort()
        print(points)
        arrows = 1
        points_ren = points[1:]
        xstart = points[0][0]
        xend = points[0][1]
        for point in points_ren:
            if point[0] >= xstart and point[0] <= xend:
                xstart = max(xstart, point[0])
                xend = min(xend, point[1])
            else:
                arrows = arrows + 1
                xstart = point[0]
                xend = point[1]

        #  approach 2:
        # points.sort(key=lambda e: e[1]);   #sort according xend
        #
        # count = 1
        # end = points[0][1];
        # for p in points:
        #     if p[0] > end:
        #         count += 1
        #         end = p[1]
        # return count

        return arrows

# [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]   output: 2
# [[0, 6], [0, 9], [2, 8], [2, 9], [3, 8], [3, 9], [3, 9], [6, 8], [7, 12], [9, 10]]
# points=[[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
# points.sort()
# print(points)

# points = [[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]
# # # [[1, 10], [3, 9], [4, 11], [6, 7], [6, 9], [8, 12], [9, 12]]
# points = sorted(points, key=lambda x: x[1])
# print(points)

# Example1:
# Input: points = [[10, 16], [2, 8], [1, 6], [7, 12]]
# Output: 2
# Explanation: One way is to shoot one arrow
# for example at x = 6 (bursting the balloons[2, 8] and[1, 6]) and another arrow at x = 11 (bursting the other two balloons).
#
# Example2:
# Input: points = [[1, 2], [3, 4], [5, 6], [7, 8]]
# Output: 4
#
# Example3:
# Input: points = [[1, 2], [2, 3], [3, 4], [4, 5]]
# Output: 2
#
# Example4:
# Input: points = [[1, 2]]
# Output: 1
#
# Example5:
# Input: points = [[2, 3], [2, 3]]
# Output: 1
