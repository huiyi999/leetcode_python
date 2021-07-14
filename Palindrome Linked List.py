# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def ReverseList(self, head: ListNode) -> ListNode:
        new_node = None
        while head:
            tmp = head
            head = head.next
            tmp.next = new_node
            new_node = tmp
        return new_node

    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        rhead = self.ReverseList(slow)
        # print(rhead)
        while rhead:
            if head.val != rhead.val:
                return False
            head = head.next
            rhead = rhead.next
        return True

    def isPalindrome2(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        size = 0
        curr = head

        while curr:
            size += 1
            curr = curr.next

        # print(size)

        prev = None
        curr = head

        i = 0
        while i != size // 2:
            next1 = curr.next
            curr.next = prev
            prev = curr
            curr = next1
            i += 1
        first_half_start = prev
        second_half_start = curr
        # print("head",head)
        # print("tail",tail)

        if size % 2 != 0:
            t = second_half_start.next
            h = first_half_start
        else:
            t = second_half_start
            h = first_half_start

        while t and h:
            if t.val != h.val: return False
            t = t.next
            h = h.next
        return True


'''
iven a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?


'''
