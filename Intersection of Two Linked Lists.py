'''
Write a program to find the node at which the intersection of two singly linked lists begins.

Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Each value on each linked list is in the range [1, 10^9].
Your code should preferably run in O(n) time and use only O(1) memory.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode2(self, headA, headB):
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = headB if not p1 else p1.next
            p2 = headA if not p2 else p2.next
        return p1

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lengthA = 0
        lengthB = 0
        nodeA = headA
        nodeB = headB
        while nodeA:
            nodeA = nodeA.next
            lengthA += 1
        while nodeB:
            nodeB = nodeB.next
            lengthB += 1
        if lengthA > lengthB:
            n = lengthA - lengthB
            nodeA = headA
            while n:
                nodeA = nodeA.next
                n -= 1
        elif lengthA < lengthB:
            n = lengthB - lengthA
            nodeB = headB
            while n:
                nodeB = nodeB.next
                n -= 1
        while nodeA != nodeB:
            nodeA = nodeA.next
            nodeB = nodeB.next

        return nodeA


'''


'''
