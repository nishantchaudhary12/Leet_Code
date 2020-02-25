'''A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        stack = [root]
        val = root.val
        temp = root
        while stack:
            while temp.left:
                stack.append(temp.left)
                temp = temp.left
            temp = stack.pop()
            # print(temp.val)
            if temp.val != val:
                return False
            if temp.right:
                stack.append(temp.right)
                temp = temp.right
        return True