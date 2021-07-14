'''
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    '''
    approach 2
    '''
    def sortList2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        p = head
        node_list = []
        while head:
            node_list.append(head.val)
            head = head.next

        node_list.sort()
        head = p
        for i in node_list:
            head.val = i
            head = head.next

        return p

    '''
    approach 1 merge sort
    '''
    def MergeTwoSortedLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1

        head = ListNode(0)
        ne = head

        while l1 and l2:
            if l1.val <= l2.val:
                ne.next = l1
                l1 = l1.next
            else:
                ne.next = l2
                l2 = l2.next
            ne = ne.next
        ne.next = l1 if l1 else l2
        return head.next

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        pre = head
        slow = head  # 使用快慢指针来确定中点
        fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        left = head
        right = pre.next    #the beginning of right part
        pre.next = None  # 从中间打断链表  the end of left part
        left = self.sortList(left)
        right = self.sortList(right)
        return self.MergeTwoSortedLists(left, right)


'''
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Input: head = []
Output: []



'''
