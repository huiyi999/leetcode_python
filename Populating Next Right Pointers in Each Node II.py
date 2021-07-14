'''
Given a binary tree
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

'''



'''
BFS, 依次将每层的节点放入列表中, 然后每个列表的节点都指向它下一个节点.
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
        if not root: return None
        q = [root]
        while q:
            for i in range(1, len(q)):
                q[i-1].next = q[i]
            q = [kid for node in q for kid in (node.left, node.right) if kid]
            # for node in q:
            #     for kid in (node.left, node.right):
            #         if kid:
            #             q=[kid]


        return root










'''
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A),
your function should populate each next pointer to point to its next right node, just like in Figure B.
The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

'''
