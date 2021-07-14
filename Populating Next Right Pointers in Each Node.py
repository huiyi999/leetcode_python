'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
The binary tree has the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.


Follow up:
You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

Constraints:
The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000
'''


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        self._connect(root, None)
        return root

    def _connect(self, root, sibling):
        if root is None:
            return
        else:
            root.next = sibling

        self._connect(root.left, root.right)

        if sibling is not None:
            self._connect(root.right, sibling.left)
        else:
            self._connect(root.right, None)

    def connect2(self, root: 'Node') -> 'Node':
        if not root:
            return root

        leftmost = root

        while leftmost.left:
            head = leftmost

            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left

        return root


'''
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A),
your function should populate each next pointer to point to its next right node,
just like in Figure B.
The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
'''
