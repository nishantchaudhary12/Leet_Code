'''Given a singly linked list, determine if it is a palindrome.'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nodes = list()
        temp = head
        prev = head
        while temp and temp.next:
            temp = temp.next.next
            prev = prev.next
        while prev:
            nodes.append(prev.val)
            prev = prev.next
        temp = head
        # print(nodes)
        while nodes:
            if temp.val != nodes.pop():
                return False
            temp = temp.next
        return True