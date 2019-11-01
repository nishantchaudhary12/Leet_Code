'''Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        queue = list()
        temp = root
        queue.append(temp)
        minDiff = sys.maxsize
        while queue:
            curr = queue.pop(0)
            if curr.left:
                queue.append(curr.left)
                minDiff = min(minDiff, curr.val - curr.left.val)
            if curr.right:
                queue.append(curr.right)
                minDiff = min(minDiff, curr.right.val - curr.val)

        return minDiff