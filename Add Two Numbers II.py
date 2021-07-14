'''
You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2: return
        if not l1: return l2
        if not l2: return l1

        num1 = ""
        num2 = ""
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        num1 = int(num1)
        num2 = int(num2)
        nums = list(str(num1 + num2))

        l = ListNode(int(nums[0]))
        res = l

        for num in nums[1:]:
            l.next = ListNode(int(num))
            l = l.next

        l = res
        return l

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = 0
        b = 0
        head1, head2 = l1, l2
        while head1:
            a = a * 10 + head1.val
            head1 = head1.next
        while head2:
            b = b * 10 + head2.val
            head2 = head2.next
        res = a + b
        new_head = None
        if res == 0:
            node = ListNode(0)
            node.next = new_head
            new_head = node
            return new_head
        while res:
            val = res % 10
            res = res // 10
            node = ListNode(val)
            node.next = new_head
            new_head = node
        return new_head


'''
Example:
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''
