'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        result = dummy

        flag = 0
        while l1 or l2:
            sum = flag
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            if sum >= 10:
                flag = 1
                sum -= 10
            else:
                flag = 0
            result.next = ListNode(sum)
            result = result.next
        if flag:
            result.next = ListNode(1)

        # while l1 or l2 or carry:
        #     val1  = (l1.val if l1 else 0)
        #     val2  = (l2.val if l2 else 0)
        #     carry, out = divmod(val1+val2 + carry, 10)
        #     #The divmod() function returns a tuple containing the quotient and the remainder
        #     #when argument1 (dividend) is divided by argument2 (divisor).
        #
        #     result_tail.next = ListNode(out)
        #     result_tail = result_tail.next
        #
        #     l1 = (l1.next if l1 else None)
        #     l2 = (l2.next if l2 else None)
        return dummy.next


'''
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

'''
