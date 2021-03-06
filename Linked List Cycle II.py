'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list
that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.

Follow up:
Can you solve it using O(1) (i.e. constant) memory?

Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle2(self, head):
        if head == None: return None
        if head.next == None: return None

        first = head.next
        second = head.next.next

        while first != second:

            if first == None: return None
            if first.next == None: return None
            if second == None: return None
            if second.next == None: return None

            first = first.next
            second = second.next.next

        first = head

        while first != second:
            first = first.next
            second = second.next
        return first

    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next: return None
        visited = []
        node = head
        while node != None:
            if node not in visited:
                visited.append(node)
                node = node.next
            else:
                return node

        return None


'''
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
'''
