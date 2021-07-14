# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 定义fast  slow，fast先走n步，然后fast slow同时往后遍历，当fast走到结尾处时，slow位于倒数第n处


        fast = slow = head

        for i in range(n):  # fast先走n步
            fast = fast.next
        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next


        slow.next =slow.next.next

        return head
