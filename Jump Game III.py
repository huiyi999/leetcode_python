'''
Given an array of non-negative integers arr, you are initially positioned at start index of the array.
When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

Constraints:
1 <= arr.length <= 5 * 10^4
0 <= arr[i] < arr.length
0 <= start < arr.length
'''
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [False] * len(arr)
        visited[start] = True

        def dfs(index):
            if arr[index] == 0:
                return True
            if index + arr[index] < len(arr) and not visited[index + arr[index]]:
                visited[index + arr[index]] = True
                if dfs(index + arr[index]):
                    return True
            if index - arr[index] > -1 and not visited[index - arr[index]]:
                visited[index - arr[index]] = True
                if dfs(index - arr[index]):
                    return True
            return False

        return dfs(start)

    def canReach2(self, arr: List[int], start: int) -> bool:
        visit = [0 for _ in range(len(arr))]

        def recursion(start, ):
            if start >= len(arr) or start < 0 or visit[start] == True:
                return False
            if arr[start] == 0:
                return True
            start1 = start + arr[start]
            start2 = start - arr[start]
            visit[start] = True
            return recursion(start1) or recursion(start2)

        return recursion(start)

    def canReach3(self, A: List[int], i: int) -> bool:
        if 0 <= i < len(A) and A[i] >= 0:
            A[i] = -A[i]
            return A[i] == 0 or self.canReach(A, i + A[i]) or self.canReach(A, i - A[i])
        return False


'''
Example 1:
Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation:
All possible ways to reach at index 3 with value 0 are:
index 5 -> index 4 -> index 1 -> index 3
index 5 -> index 6 -> index 4 -> index 1 -> index 3

Example 2:
Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true
Explanation:
One possible way to reach at index 3 with value 0 is:
index 0 -> index 4 -> index 1 -> index 3

Example 3:
Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.

'''
