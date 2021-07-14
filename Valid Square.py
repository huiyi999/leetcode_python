'''
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.
Note:
All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.

'''
from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        points = sorted(points, key=lambda x: (x[0], x[1]))

        def distance(point1, point2):
            res = (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
            return res

        return distance(points[0], points[1]) != 0 and distance(points[0], points[1]) == distance(points[1], points[
            3]) and distance(points[3], points[2]) == distance(points[0], points[2]) and distance(points[0], points[
            3]) == distance(points[2], points[1])

    def validSquare2(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(P, Q):
            return (P[0] - Q[0]) ** 2 + (P[1] - Q[1]) ** 2

        D = [dist(p1, p2), dist(p1, p3), dist(p1, p4),
             dist(p2, p3), dist(p2, p4), dist(p3, p4)]
        D.sort()
        return 0 < D[0] == D[1] == D[2] == D[3] and 2 * D[0] == D[4] == D[5]


solution = Solution()
print(solution.validSquare([0, 0], [1, 1], [1, 0], [0, 1]))
print(solution.validSquare([0, 0], [5, 0], [5, 4], [0, 4]))  # false
'''
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
'''
