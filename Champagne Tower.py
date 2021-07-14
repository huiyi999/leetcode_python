'''
We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses,
and so on until the 100th row.  Each glass holds one cup (250ml) of champagne.

Then, some champagne is poured in the first glass at the top.
When the topmost glass is full,
any excess liquid poured will fall equally to the glass immediately to the left and right of it.
When those glasses become full, any excess champagne will fall equally to the left and right of those glasses,
and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is full.
After two cups of champagne are poured, the two glasses on the second row are half full.
After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.
After four cups of champagne are poured, the third row has the middle glass half full,
and the two outside glasses are a quarter full, as pictured below.

Now after pouring some non-negative integer cups of champagne,
return how full the jth glass in the ith row is (both i and j are 0-indexed.)
'''


class Solution:
    #  wrong computation
    # def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
    #     index = [query_row, query_glass - 1]
    #     cups = 0
    #     for i in range(1, query_row + 1):
    #         cups += i
    #     print("total cups: ", cups)
    #     if (poured <= cups):
    #         return float(0)
    #     elif (poured >= (cups + query_row + 1)):
    #         return float(1)
    #     else:
    #         remain = poured - cups
    #         cup = remain / query_row
    #         print(cup)
    #         if query_glass == 1 or query_glass == query_row:
    #             return float(cup / 2)
    #         else:
    #             return float(cup)

    def champagneTower2(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        N = 100
        dp = [[0] * N for _ in range(N)]
        dp[0][0] = poured
        for i in range(query_row):
            for j in range(i + 1):
                if dp[i][j] > 1:
                    dp[i + 1][j    ] += (dp[i][j] - 1) / 2.0
                    dp[i + 1][j + 1] += (dp[i][j] - 1) / 2.0
        return min(1, dp[query_row][query_glass])



solution = Solution()
print(solution.champagneTower2(1, 1, 1))
print(solution.champagneTower2(2, 1, 1))
print(solution.champagneTower2(100000009, 33, 17))
print(solution.champagneTower2(25, 6, 1))
# print(solution.champagneTower(8, 3, 1))
# print(solution.champagneTower(8, 3, 0))
print(solution.champagneTower2(8, 3, 0))
print(solution.champagneTower2(8, 3, 1))

'''
Example 1:
Input: poured = 1, query_row = 1, query_glass = 1
Output: 0.00000
Explanation: We poured 1 cup of champange to the top glass of the tower
(which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.

Example 2:
Input: poured = 2, query_row = 1, query_glass = 1
Output: 0.50000
Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)).
There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.

Example 3:
Input: poured = 100000009, query_row = 33, query_glass = 17
Output: 1.00000
'''
