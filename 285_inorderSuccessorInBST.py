'''Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        def findNode(node):
            if node == p:
                return
            if node.val < p.val:
                stack.append(node)
                node = node.right
            else:
                stack.append(node)
                node = node.left
            findNode(node)

        if p.right:
            temp = p.right
            while temp.left:
                temp = temp.left
            return temp

        stack = list()
        findNode(root)
        minCurr = 2 ** 31 - 1
        ans = 0
        while stack:
            curr = stack.pop()
            if curr.val > p.val and curr.val < minCurr:
                minCurr = curr.val
                ans = curr
        return ans if ans else None