# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        last = None

        while head:
            tmp = head.next
            head.next = last
            last = head
            head = tmp
        return last

    def reverseList2(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while (cur):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
