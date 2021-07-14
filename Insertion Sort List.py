'''
Sort a linked list using insertion sort.

Algorithm of Insertion Sort:
Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data,
finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList2(self, head: ListNode) -> ListNode:
        nodeDict = []
        res = pre = ListNode(0)
        while head:
            nodeDict.append([head.val, head])
            head = head.next
        sortedDict = sorted(nodeDict, key=(lambda x: x[0]))
        for key, value in sortedDict:
            pre.next = value
            pre = pre.next
        pre.next = None
        return res.next

    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = dummy = ListNode(-1)
        while head:
            while cur.next and cur.next.val < head.val:  # 找到插入点
                cur = cur.next
            # 插入新的结点
            cur_next = cur.next
            head_next = head.next
            cur.next = head
            cur.next.next = cur_next
            head = head_next

            cur = dummy

        return dummy.next


'''
Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''
