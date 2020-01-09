'''Given a binary tree, determine if it is a complete binary tree.'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        node = [(root, 1)]
        i = 0
        while i < len(node):
            curr, j = node[i]
            i += 1
            if curr:
                node.append((curr.left, 2 * j))
                node.append((curr.right, 2 * j + 1))
        # print(node)
        return node[-1][1] == len(node)


