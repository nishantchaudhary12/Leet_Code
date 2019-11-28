'''Given a binary tree, return the inorder traversal of its nodes' values.'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = list()
        temp = root
        result = list()
        while True:
            while temp:
                stack.append(temp)
                temp = temp.left
            curr = stack.pop()
            result.append(curr.val)
            if curr.right:
                temp = curr.right
            elif not temp and not stack:
                break
        return result