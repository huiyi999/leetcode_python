'''
Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

Constraints:
The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.


'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    sum = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.preOrder(root, low, high)
        return self.sum

    def preOrder(self, root: TreeNode, low: int, high: int):
        if root:
            if root.val >= low and root.val <= high:
                self.sum += root.val
            self.preOrder(root.left, low, high)
            self.preOrder(root.right, low, high)

    def rangeSumBST2(self, root: TreeNode, L: int, R: int) -> int:
        self.ans = 0

        def dfs(head):
            if head:
                if L <= head.val <= R:
                    self.ans += head.val
                if L < head.val:
                    dfs(head.left)
                if head.val < R:
                    dfs(head.right)

        dfs(root)
        return self.ans


'''
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32

Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23

'''
