'''
There is a special square room with mirrors on each of the four walls.
Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p, and a laser ray from the southwest corner
first meets the east wall at a distance q from the 0th receptor.

Return the number of the receptor that the ray meets first.
(It is guaranteed that the ray will meet a receptor eventually.)

Note:
1 <= p <= 1000
0 <= q <= p
'''
import math
'''
想象一下，把这样的正方体一直往上摞，问题就变成了光线反复横跳，看它最先跳到哪那个顶点。因此求p,q的最小公倍数，最小公倍数等于pq\gcd(p,q)，
通过计算走了几步 p 和走了几步 q 来确定到达位置。
'''

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        m, n = q, p
        while m % 2 == 0 and n % 2 == 0:
            m, n = m / 2, n / 2
        if m % 2 == 0 and n % 2 == 1:
            return 0
        elif m % 2 == 1 and n % 2 == 1:
            return 1
        elif m % 2 == 1 and n % 2 == 0:
            return 2

    def mirrorReflection2(self, p: int, q: int) -> int:
        x = p // math.gcd(p, q)
        y = q // math.gcd(p, q)

        if x % 2 == 1 and y % 2 == 1:
            return 1
        elif x % 2 == 0 and y % 2 == 1:
            return 2
        else:
            return 0


'''
Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.
'''
