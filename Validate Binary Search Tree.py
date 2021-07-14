'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # '''
    # [0]  excepted; true  output: false
    # '''
    # pre = TreeNode()
    # def isValidBST(self, root: TreeNode) -> bool:
    #     if root:
    #         if not self.isValidBST(root.left):
    #             return False
    #         if self.pre and root.val <= self.pre.val:
    #             return False
    #         self.pre = root
    #
    #         return self.isValidBST(root.right)
    #     return True

    def isValidBS2T(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.valid(root, float('-inf'), float('inf'))

    def valid(self, root, min, max):
        if not root: return True
        if root.val >= max or root.val <= min:
            return False
        return self.valid(root.left, min, root.val) and self.valid(root.right, root.val, max)


    def isValidBST3(self, root: TreeNode) -> bool:
        def rec(root, a, b):
            return not root or (a < root.val < b and rec(root.left,a, root.val) and rec(root.right, root.val, b))

        return rec(root, float("-inf"), float("inf"))

'''
Input: root = [2,1,3]
Output: true

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

'''
