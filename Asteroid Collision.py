'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size,
and the sign represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode.
If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Constraints:
1 <= asteroids <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
'''
from typing import List

'''
当stack中最后一个行星为正，当前加入为负时需要处理

'''


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0:
                    if stack[-1] < -asteroid:  # 负的size > 正的size，删除正的
                        stack.pop()
                    elif stack[-1] == -asteroid:  # 负的size = 正的size，删除正的
                        stack.pop()
                        break
                    else:  # 负的size < 正的size,不加入，跳过
                        break
                else:  # With the else statement we can run a block of code once when the condition no longer is true:
                    stack.append(asteroid)

        stack2 = []
        for e in asteroids:
            if not stack2 or stack2[-1] < 0 or e > 0:
                stack2.append(e)

            else:
                flag = True
                while stack2 and stack2[-1] > 0 and stack2[-1] <= -e:
                    tmp = stack2.pop()
                    if tmp == -e:
                        flag = False
                        break
                if (not stack2 or stack2[-1] < 0) and flag:
                    stack2.append(e)

        return stack


solution = Solution()
print(solution.asteroidCollision([5, 10, -5]))
print(solution.asteroidCollision([8, -8]))
print(solution.asteroidCollision([10, 2, -5]))
print(solution.asteroidCollision([-2, -1, 1, 2]))

'''
Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.

Example 2:
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

Example 4:
Input: asteroids = [-2,-1,1,2]
Output: [-2,-1,1,2]
Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each other.
'''
