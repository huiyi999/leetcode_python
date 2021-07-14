# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # left = 0
        # right = n - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if isBadVersion(mid):
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return left


        # good = 0
        # bad = n
        #
        # while bad - good > 1:
        #     mid = (good+bad)//2
        #
        #     if isBadVersion(mid):
        #         bad = mid
        #     else:
        #         good = mid
        #
        # return bad


'''
Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1

'''
