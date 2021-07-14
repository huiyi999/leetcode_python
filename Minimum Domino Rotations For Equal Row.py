'''
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

Constraints:
2 <= A.length == B.length <= 2 * 104
1 <= A[i], B[i] <= 6
'''
from typing import List


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        ans1 = self.rotate(A, B)
        ans2 = self.rotate(B, A)
        if ans1 != -1 and ans2 != -1:
            return min(ans1, ans2)
        elif ans1 != -1 and ans2 == -1:
            return ans1
        elif ans1 == -1 and ans2 != -1:
            return ans2
        else:
            return -1

    def rotate(self, first: List[int], second: List[int]):
        l_dict = dict()
        for i, num in enumerate(first):
            if num in l_dict:
                tmp = l_dict[num]
                tmp.append(i)
            else:
                tmp = [i]
                l_dict[num] = tmp

        max_a = 0
        for key, value in l_dict.items():
            if len(value) >= max_a:
                max_a = len(value)
                rotate = key
        time = 0
        for i, num in enumerate(first):
            if num != rotate:
                if second[i] == rotate:
                    time = time + 1
                else:
                    return -1
        return time

    def minDominoRotations2(self, A: List[int], B: List[int]) -> int:
        assert (len(A) >= 2)

        def check(x):
            """
            Return min number of swaps
            if one could make all elements in A or B equal to x.
            Else return -1.
            """
            # how many rotations should be done
            # to have all elements in A equal to x
            # and to have all elements in B equal to x
            rotations_a = rotations_b = 0
            for i in range(n):
                # rotations coudn't be done
                if A[i] != x and B[i] != x:
                    return -1
                # A[i] != x and B[i] == x
                elif A[i] != x:
                    rotations_a += 1
                # A[i] == x and B[i] != x
                elif B[i] != x:
                    rotations_b += 1
            # min number of rotations to have all
            # elements equal to x in A or B
            return min(rotations_a, rotations_b)

        n = len(A)
        rotations = check(A[0])
        # If one could make all elements in A or B equal to A[0]
        if rotations != -1:
            return rotations
            # If one could make all elements in A or B equal to B[0]
        else:
            return check(B[0])

    def minDominoRotations3(self, A: List[int], B: List[int]) -> int:
        for x in [A[0], B[0]]:
            if all(x in d for d in zip(A, B)):
                return len(A) - max(A.count(x), B.count(x))
        return -1

    def minDominoRotations4(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        di = {}
        for i in range(len(A)):
            if A[i] in di:
                di[A[i]] += 1
            if B[i] in di and B[i] != A[i]:
                di[B[i]] += 1
            if B[i] not in di:
                di[B[i]] = 1
            if A[i] not in di:
                di[A[i]] = 1
        if max(di.values()) < len(A):
            return (-1)
        else:
            print('4:')
            print(max(di, key=di.get))  # di.get=value, select the key with maximum value
            return (min(len(A) - B.count(max(di, key=di.get)), len(A) - A.count(max(di, key=di.get))))


solution = Solution()
print(solution.minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]))
print(solution.minDominoRotations4([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]))
print(solution.minDominoRotations([3, 5, 1, 2, 3], [3, 6, 3, 3, 4]))
'''
Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

Example 2:
Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
'''
