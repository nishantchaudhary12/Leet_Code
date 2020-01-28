'''A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        def makeCopy(node):
            if not node:
                return None
            if node in visited:
                return visited[node]
            new = Node(node.val, None, None)
            visited[node] = new

            # if node.next:
            new.next = makeCopy(node.next)

            new.random = makeCopy(node.random)

            return new

        visited = dict()
        return makeCopy(head)

