'''You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        temp = l3
        carry = 0
        while l1 or l2:
            if l1 and l2:
                curr = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                curr = l1.val + carry
                l1 = l1.next
            else:
                curr = l2.val + carry
                l2 = l2.next
            carry = curr // 10
            l3.next = ListNode(curr % 10)
            l3 = l3.next
        if carry:
            l3.next = ListNode(carry)
        return temp.next

