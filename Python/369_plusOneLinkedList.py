'''Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        temp = ListNode(0)
        temp.next = head
        curr = prev = temp

        while curr:
            if curr.val < 9:
                prev = curr
            curr = curr.next

        prev.val += 1
        while prev.next:
            prev = prev.next
            prev.val = 0

        return temp if temp.val == 1 else temp.next 