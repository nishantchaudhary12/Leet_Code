'''Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def _iterate(node):
            if not node:
                return 0
            left = _iterate(node.left)
            right = _iterate(node.right)
            return max(left, right) + 1

        if not root:
            return 0
        return _iterate(root)



