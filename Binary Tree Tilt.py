'''
Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all left subtree node values
and all right subtree node values.
If a node does not have a left child, then the sum of the left subtree node values is treated as 0.
The rule is similar if there the node does not have a right child.

Constraints:
The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000


'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result = 0

    def findTilt(self, root: TreeNode) -> int:
        self.postOrder(root)
        return self.result

    def postOrder(self, root: TreeNode):
        if not root:
            return 0
        left = self.postOrder(root.left)
        right = self.postOrder(root.right)
        self.result += abs(left - right)
        return left + right + root.val
