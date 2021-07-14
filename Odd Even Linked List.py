'''

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        odd = head
        evenHead = head.next
        evenTail = head.next
        node = evenTail.next
        isOdd = True
        while node:
            if isOdd:
                odd.next = node
                odd = odd.next
            else:
                evenTail.next = node
                evenTail = evenTail.next

            node = node.next
            isOdd = not isOdd
        evenTail.next = None
        odd.next = evenHead
        return head

    def oddEvenList2(self, head: ListNode) -> ListNode:
        if not head:
            return None
        odd, even = head, head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head

    def oddEvenList3(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head
        oddTail, evenHead, evenTail = head, head.next, head.next
        curr = evenHead.next
        isOdd = True
        while curr:
            if isOdd:
                temp = curr.next
                oddTail.next = curr
                curr.next = evenHead
                evenTail.next = temp
                curr = temp
                oddTail = oddTail.next
                evenTail = evenTail.next
            else:
                curr = curr.next
            isOdd = not isOdd
        return head


'''
Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL


 '''
