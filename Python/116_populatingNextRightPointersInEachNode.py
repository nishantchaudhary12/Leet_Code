'''You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node,
the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root

        stack = [root]
        while stack:
            currLevel = list()
            for i, each in enumerate(stack):
                if i < len(stack) - 1:
                    each.next = stack[i + 1]
                if each.left:
                    currLevel.append(each.left)
                if each.right:
                    currLevel.append(each.right)
            stack = currLevel
        return root



