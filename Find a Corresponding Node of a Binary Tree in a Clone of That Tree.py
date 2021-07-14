'''

Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

Follow up: Solve the problem if repeated values on the tree are allowed.


'''

'''
在cloned里面找到与target值相同的节点就可以了，因此只需要遍历树就好了。对于进阶，如果出现相同的值，就需要根据原树判断。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = []
        while cloned or stack:
            while cloned:
                stack.append(cloned)
                cloned = cloned.left
            cloned = stack.pop()
            if cloned.val == target.val:
                return cloned
            cloned = cloned.right

    def getTargetCopy2(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None
        if original == target:
            return cloned
        L = self.getTargetCopy(original.left, cloned.left, target)
        if L:
            return L
        return self.getTargetCopy(original.right, cloned.right, target)


'''
Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown.
The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.

Input: tree = [7], target =  7
Output: 7

Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
Output: 4

Input: tree = [1,2,3,4,5,6,7,8,9,10], target = 5
Output: 5

Input: tree = [1,2,null,3], target = 2
Output: 2



'''
