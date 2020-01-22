'''Given a rooted binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0, and if the depth of a node is d, the depth of each of its children is d+1.
The lowest common ancestor of a set S of nodes is the node A with the largest depth such that every node in S is in the subtree with root A.'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def _helper(node, depth):
            self.depth = max(self.depth, depth)
            if not node:
                return depth
            left = _helper(node.left, depth + 1)
            right = _helper(node.right, depth + 1)
            if left == right == self.depth:
                self.res = node
            return max(left, right)

        if not root: return 0
        self.res = root
        self.depth = -1
        _helper(root, 0)
        # print(self.res.val)
        return self.res