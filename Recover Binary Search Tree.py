'''
You are given the root of a binary search tree (BST),
where exactly two nodes of the tree were swapped by mistake.
Recover the tree without changing its structure.

Follow up: A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?

Constraints:
The number of nodes in the tree is in the range [2, 1000].
-231 <= Node.val <= 231 - 1
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.pre, self.first, self.second = None, None, None
        self.inOrder(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def inOrder(self, root):
        if not root: return

        self.inOrder(root.left)
        if self.pre and self.pre.val > root.val:
            if not self.first:
                self.first = self.pre
            self.second = root
        self.pre = root
        self.inOrder(root.right)

    def recoverTree2(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def search(root):
            nonlocal x, y, prev

            if not root:
                return

            search(root.left)
            if prev and prev.val > root.val:
                if not y:
                    x = prev
                    y = root
                else:
                    y = root
                    return

            prev = root
            search(root.right)

        x, y, prev = None, None, None
        search(root)
        x.val, y.val = y.val, x.val

    def recoverTree3(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        stack = []
        self.addLeftNodes(stack, root)
        prev = None
        swapNodes = [None, None]

        while stack:
            node = stack.pop()
            if prev and node.val < prev.val:
                swapNodes[0] = node
                if swapNodes[1] is None:
                    swapNodes[1] = prev
                else:
                    break
            prev = node
            self.addLeftNodes(stack, node.right)

        swapNodes[0].val, swapNodes[1].val = swapNodes[1].val, swapNodes[0].val

    def addLeftNodes(self, stack, root):
        while root:
            stack.append(root)
            root = root.left

'''
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
'''
