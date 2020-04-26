#Invert a binary tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def _helper(node):
            if not node:
                return None
            node.left, node.right = _helper(node.right), _helper(node.left)
            return node

        return _helper(root)

