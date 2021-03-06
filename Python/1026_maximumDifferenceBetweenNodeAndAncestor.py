'''Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where
V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def _iterate(node, high, low):
            if not node:
                return high - low
            else:
                high = max(high, node.val)
                low = min(low, node.val)
                return max(_iterate(node.left, high, low), _iterate(node.right, high, low))

        if not root: return 0
        return _iterate(root, root.val, root.val)
