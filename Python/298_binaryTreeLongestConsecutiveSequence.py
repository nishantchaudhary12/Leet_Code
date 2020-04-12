'''Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
The longest consecutive path need to be from parent to child (cannot be the reverse).'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.longest = 1

    def longestConsecutive(self, root: TreeNode) -> int:
        def _helper(node, curr):
            if node.left:
                if node.left.val == node.val + 1:
                    _helper(node.left, curr + 1)
                else:
                    _helper(node.left, 1)
            if node.right:
                if node.right.val == node.val + 1:
                    _helper(node.right, curr + 1)
                else:
                    _helper(node.right, 1)
            self.longest = max(self.longest, curr)

        if not root: return 0
        _helper(root, 1)
        return self.longest