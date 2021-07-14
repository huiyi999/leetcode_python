'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
Follow up: Could you solve it both recursively and iteratively?
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.mirror(root.left, root.right)

    def mirror(self, left: TreeNode, right: TreeNode):
        if not left or not right:
            return left == right
        elif left.val != right.val:
            return False
        else:
            return self.mirror(left.left, right.right) and self.mirror(left.right, right.left)

    def isSymmetric2(self, root: TreeNode) -> bool:
        def DFS(r1, r2):
            if not r1 and not r2:
                return True
            if bool(r1) != bool(r2):
                return False
            if r1.val != r2.val:
                return False
            left = DFS(r1.left, r2.right)
            right = DFS(r1.right, r2.left)
            return left and right

        return DFS(root, root)


'''
Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false
'''
