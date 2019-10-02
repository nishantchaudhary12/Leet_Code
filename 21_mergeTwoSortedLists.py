'''Merge two sorted linked lists and return it as a new list. The new list should be made by
splicing together the nodes of the first two lists.'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i = l1
        j = l2
        if i and j:
            if i.val <= j.val:
                l3 = ListNode(i.val)
                i = i.next
            else:
                l3 = ListNode(j.val)
                j = j.next
            temp = l3
            while i and j:
                # print()
                if i.val <= j.val:
                    temp.next = i
                    temp = temp.next
                    i = i.next
                else:
                    temp.next = j
                    temp = temp.next
                    j = j.next
            while i:
                temp.next = i
                temp = temp.next
                i = i.next
            while j:
                temp.next = j
                temp = temp.next
                j = j.next
            return l3
        elif i:
            return i
        elif j:
            return j
        else:
            return None
