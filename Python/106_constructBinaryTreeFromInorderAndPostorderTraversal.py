'''Given inorder and postorder traversal of a tree, construct the binary tree.'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def _helper(inorder, postorder):
            if not inorder:
                return
            curr = postorder.pop()
            node = TreeNode(curr)
            i = inorder.index(curr)
            node.right = _helper(inorder[i + 1:], postorder)
            node.left = _helper(inorder[:i], postorder)
            return node

        return _helper(inorder, postorder)
