'''
Given the root of a binary tree, find the maximum value V for
which there exist different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.

Constraints:
The number of nodes in the tree is in the range [2, 5000].
0 <= Node.val <= 105
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_value = 0

    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.preOrder(root)
        return self.max_value

    def preOrder(self, root):
        if root:
            A_value = root.val
            # self.preOrder(root)
            self.max_diff(root, A_value)
            self.preOrder(root.left)
            # self.max_diff(root.left, A_value)
            self.preOrder(root.right)
            # self.max_diff(root.right, A_value)

    def max_diff(self, root, A_value):
        if not root: return 0
        print(A_value, self.max_value)
        if root.left:
            left = root.left.val
            self.max_value = max(self.max_value, abs(A_value - left))
            self.max_diff(root.left, A_value)
            self.max_diff(root.right, A_value)

        if root.right:
            right = root.right.val
            self.max_value = max(self.max_value, abs(A_value - right))
            self.max_diff(root.left, A_value)
            self.max_diff(root.right, A_value)

    def maxAncestorDiff2(self, root: TreeNode) -> int:

        if not root:
            return 0

        self.ans = float('-inf')

        def helper(node):

            val = node.val
            if not node.left and not node.right:
                return val, val

            lo, hi = val, val
            if node.left:
                lwr, upper = helper(node.left)
                diff = max(abs(val - lwr), abs(val - upper))
                self.ans = max(self.ans, diff)
                lo = min(lwr, lo)
                hi = max(upper, hi)
            if node.right:
                lwr, upper = helper(node.right)
                diff = max(abs(val - lwr), abs(val - upper))
                self.ans = max(self.ans, diff)
                lo = min(lwr, lo)
                hi = max(upper, hi)
            return lo, hi

        helper(root)
        return self.ans

'''
Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

Input: root = [1,null,2,null,0,3]
Output: 3
'''
