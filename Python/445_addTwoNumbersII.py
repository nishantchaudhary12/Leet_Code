'''You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = list()
        stack2 = list()
        while l1 or l2:
            if l1:
                stack1.append(l1.val)
                l1 = l1.next
            if l2:
                stack2.append(l2.val)
                l2 = l2.next

        node = ListNode(0)
        temp = node
        carry = 0
        while stack1 or stack2:
            first = stack1.pop() if stack1 else 0
            second = stack2.pop() if stack2 else 0
            curr = first + second + carry
            temp = node.next
            new = ListNode(curr % 10)
            node.next = new
            new.next = temp
            carry = curr // 10

        if carry:
            temp = node.next
            new = ListNode(carry)
            node.next = new
            new.next = temp

        return node.next