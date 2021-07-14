'''
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.
Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

Constraints:
1 <= time.length <= 6 * 104
1 <= time[i] <= 500

'''
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0

        matrix = [0] * 60
        for duration in time:
            matrix[duration % 60] += 1

        # print(matrix)
        res += int(matrix[0] * (matrix[0] - 1) / 2)
        res += int(matrix[30] * (matrix[30] - 1) / 2)

        i = 1
        j = 59
        while i < j:
            res += matrix[i] * matrix[j]
            i += 1
            j -= 1
        return res

    def numPairsDivisibleBy602(self, time: List[int]) -> int:
        arr = [0 for _ in range(60)]
        count = 0
        for elem in time:
            arr[elem % 60] += 1

        for i in range(0, 31):
            if arr[i] == 0:
                continue
            elif (i == 0 or i == 30):

                count += int(arr[i] * (arr[i] - 1) / 2)
            else:
                count += arr[i] * arr[60-i]
        return count


solution = Solution()
print(solution.numPairsDivisibleBy60([30, 20, 150, 100, 40]))
print(solution.numPairsDivisibleBy60([60, 60, 60]))

'''
Example 1:
Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60

Example 2:
Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.

'''
