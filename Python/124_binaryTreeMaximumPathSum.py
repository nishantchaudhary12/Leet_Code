'''Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the
parent-child connections. The path must contain at least one node and does not need to go through the root.'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = - 2 ** 31

    def _iterate(self, node):
        if not node:
            return 0
        left = max(self._iterate(node.left), 0)
        right = max(self._iterate(node.right), 0)
        self.ans = max(self.ans, left + right + node.val)
        return max(left, right) + node.val

    def maxPathSum(self, root: TreeNode) -> int:
        if root:
            self._iterate(root)
        return self.ans