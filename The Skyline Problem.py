'''
https://leetcode.com/problems/the-skyline-problem/
'''
from heapq import heappush, heappop
from typing import List

'''
数据结构堆（heap）是一种优先队列。
使用优先队列能够以任意顺序增加对象，并且能在任意的时间（可能在增加对象的同时）找到（也可能移除）最小的元素，
也就是说它比python的min方法更加有效率
'''


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        # add start-building events
        # also add end-building events(acts as buildings with 0 height)
        # and sort the events in left -> right order
        events = [(L, -H, R) for L, R, H in buildings]
        events += list({(R, 0, 0) for _, R, _ in buildings})
        events.sort()
        print(events)

        # res: result, [x, height]
        # live: heap, [-height, ending position]
        res = [[0, 0]]
        live = [(0, float("inf"))]
        for pos, negH, R in events:
            # 1, pop buildings that are already ended
            # 2, if it's the start-building event, make the building alive
            # 3, if previous keypoint height != current highest height, edit the result
            while live[0][1] <= pos: heappop(live)  # heappop(heap)将数组堆中的最小元素弹出
            if negH: heappush(live, (negH, R))  # 最小的在第一个
            print(live)
            if res[-1][1] != -live[0][0]:
                res += [[pos, -live[0][0]]]
        return res[1:]


solution = Solution()
solution.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
