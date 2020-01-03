'''Given a linked list, remove the n-th node from the end of list and return its head.'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = head
        prev = head
        count = 0
        while temp.next:
            temp = temp.next
            count += 1
            if count > n:
                prev = prev.next
        if count < n:
            return head.next
        prev.next = prev.next.next
        return head