'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if root:
            queue = [root]
            while queue:
                tmp = []
                for i in range(len(queue)):
                    node = queue.pop()
                    tmp.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                if tmp:
                    ans.append(tmp)
        return ans

    def levelOrde2r(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        que = []
        que.append(root)
        count = 1
        res = []
        while len(que) != 0:
            temp = 0
            tL = []
            while count != 0:
                ele = que.pop(0)
                tL.append(ele.val)
                if ele.left:
                    temp += 1
                    que.append(ele.left)
                if ele.right:
                    temp += 1
                    que.append(ele.right)
                count -= 1
            res.append(tL)
            count = temp
        return res


'''
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

'''
