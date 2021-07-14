'''
Given the root of a binary search tree, rearrange the tree in in-order
so that the leftmost node in the tree is now the root of the tree,
and every node has no left child and only one right child.

Constraints:
The number of nodes in the given tree will be in the range [1, 100].
0 <= Node.val <= 1000
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        nodes = []

        def inorder(node):
            if node:
                inorder(node.left)
                nodes.append(node.val)
                inorder(node.right)

        inorder(root)
        head = TreeNode(nodes[0])
        res = head
        for node in nodes[1:]:
            head.right = TreeNode(node)
            head = head.right
        return res

    def increasingBST2(self, root: TreeNode) -> TreeNode:
        return self.BSTHelper(root)

    def BSTHelper(self, root, tail=None):
        if (root is None):
            return tail
        res = self.BSTHelper(root.left, root)
        root.left = None
        root.right = self.BSTHelper(root.right, tail)
        return res


'''
Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]


Input: root = [5,1,7]
Output: [1,null,5,null,7]
'''
