'''
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (x, y), its left and right children will be at positions (x - 1, y - 1) and (x + 1, y - 1) respectively.

The vertical order traversal of a binary tree is a list of non-empty reports for each unique x-coordinate from left to right.
Each report is a list of all nodes at a given x-coordinate.
The report should be primarily sorted by y-coordinate from highest y-coordinate to lowest.
If any two nodes have the same y-coordinate in the report, the node with the smaller value should appear earlier.

Return the vertical order traversal of the binary tree.

Constraints:
The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000
'''
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    positions = []

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.dfs(root, 0, 0)
        self.positions.sort(key = lambda x : (x[0], -x[1], x[2]))   # [(-1, -1, 9), (0, -2, 15), (0, 0, 3), (1, -1, 20), (2, -2, 7)]

        res = [[self.positions[0][2]]]
        for i in range(1, len(self.positions)):
            if self.positions[i][0] == self.positions[i - 1][0]:
                res[-1].append(self.positions[i][2])
            else:
                res.append([self.positions[i][2]])
        return res

    def dfs(self, node, x, y):
        if not node: return
        self.positions.append((x, y, node.val))
        self.dfs(node.left, x - 1, y - 1)
        self.dfs(node.right, x + 1, y - 1)

    def preOrder(self, node, x, y):
        if not node: return
        self.positions.append((x, y, node.val))
        self.preOrder(node.left, x - 1, y - 1)
        self.preOrder(node.right, x + 1, y - 1)

    def verticalTraversal2(self, root: TreeNode) -> List[List[int]]:
        grid = {}
        queue = [(root, 0, 0)]
        res = []
        for cur in queue:
            if cur[0]:
                horizon, lvl = cur[1], cur[2]
                if not cur[1] in grid:
                    grid[cur[1]]=[[lvl, cur[0].val]]
                else:
                    grid[cur[1]].append([lvl, cur[0].val])
                queue.append((cur[0].left, horizon-1, lvl+1))
                queue.append((cur[0].right, horizon+1, lvl+1))
        for i in sorted(grid.keys()):
            # print("i:",i)
            # print("grid[i]:",grid[i])
            res.append([value[1] for value in sorted(grid[i])])
        return res


'''
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: Without loss of generality, we can assume the root node is at position (0, 0):
The node with value 9 occurs at position (-1, -1).
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2).
The node with value 20 occurs at position (1, -1).
The node with value 7 occurs at position (2, -2).


Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report [1,5,6], the node with value 5 comes first since 5 is smaller than 6.
'''
