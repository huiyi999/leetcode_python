'''
Serialization is converting a data structure or object into a sequence of bits
so that it can be stored in a file or memory buffer,
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree.
There is no restriction on how your serialization/deserialization algorithm should work.
You need to ensure that a binary search tree can be serialized to a string,
and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The input tree is guaranteed to be a binary search tree.
'''

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        def preOrder(root):
            if root:
                res.append(str(root.val))
                preOrder(root.left)
                preOrder(root.right)

        preOrder(root)
        return ' '.join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        vals = collections.deque(val for val in data.split())

        def build(minVal, maxVal):
            if vals and minVal < vals[0] < maxVal:
                val = vals.popleft()
                root = TreeNode(val)
                root.left = build(minVal, val)
                root.right = build(val, maxVal)
                return root

        return build(float('-inf'), float('inf'))

        # 会有null
        # def build():
        #     if vals:
        #         val = vals.popleft()
        #         if val == ' ':
        #             return None
        #         root = TreeNode(int(val))
        #         root.left = build()
        #         root.right = build()
        #         return root
        #
        # return build()






# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()

# tree = ser.serialize(root)
# print(tree)
# ans = deser.deserialize(tree)
# print(ans)
# return ans


# Example1:
# Input: root = [2, 1, 3]
# Output: [2, 1, 3]
#
# Example2:
# Input: root = []
# Output: []


'''
# Inorder traversal
# Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            self.inorderTraversal(root.left)
            res.append(root.data)
            self.inorderTraversal(root.right)
        return res

# Preorder traversal
# Root -> Left ->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            self.PreorderTraversal(root.left)
            self.PreorderTraversal(root.right)
        return res

# Preorder traversal
# Root -> Left ->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            self.PreorderTraversal(root.left)
            self.PreorderTraversal(root.right)
        return res

'''
