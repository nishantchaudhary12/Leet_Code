'''Sort a linked list using insertion sort.'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        p = node = ListNode(0)
        temp = node.next = head
        while temp and temp.next:
            curr = temp.next.val
            if curr > temp.val:
                temp = temp.next
                continue
            if p.next.val > curr:
                p = node
            while p.next.val < curr:
                p = p.next
            new = temp.next
            temp.next = temp.next.next
            new.next = p.next
            p.next = new
        return node.next