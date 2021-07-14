'''
We have n chips, where the position of the ith chip is position[i].

We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to:
position[i] + 2 or position[i] - 2 with cost = 0.
position[i] + 1 or position[i] - 1 with cost = 1.
Return the minimum cost needed to move all the chips to the same position.

Constraints:
1 <= position.length <= 100
1 <= position[i] <= 10^9
'''
import sys
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:

        odd_cost = 0
        even_cost = 0

        for p in position:
            if p % 2 == 0:
                even_cost += 1
            else:
                odd_cost += 1
        print(min(odd_cost, even_cost))
        return min(odd_cost, even_cost)

    def minCostToMoveChips2(self, position: List[int]) -> int:
        odd = sum([pos % 2 for pos in position])
        return min(odd, len(position) - odd)


solution = Solution()
solution.minCostToMoveChips([1, 2, 3])
solution.minCostToMoveChips([2, 2, 2, 3, 3])
solution.minCostToMoveChips([1, 1000000000])
solution.minCostToMoveChips([10, 3, 3, 1, 6, 2, 1, 10, 6, 6])  # 4
solution.minCostToMoveChips([2, 3, 3])  # 4
'''
Input: position = [1,2,3]
Output: 1
Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
Second step: Move the chip at position 2 to position 1 with cost = 1.
Total cost is 1.

Input: position = [2,2,2,3,3]
Output: 2
Explanation: We can move the two chips at poistion 3 to position 2. Each move has cost = 1. The total cost = 2.

Input: position = [1,1000000000]
Output: 1

'''
