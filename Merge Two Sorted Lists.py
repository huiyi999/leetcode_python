# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = ListNode(0)
        l = head

        while l1 or l2:
            if not l1:
                head.next = ListNode(l2.val)
                l2 = l2.next
            elif not l2:
                head.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val < l2.val:
                head.next = ListNode(l1.val)
                l1 = l1.next
            else:
                head.next = ListNode(l2.val)
                l2 = l2.next
            head = head.next

        if l1:
            head.next = l1
        elif l2:
            head.next = l2
        return l.next


'''

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
'''
