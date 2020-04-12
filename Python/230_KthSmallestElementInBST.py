'''Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = list()
        temp = root
        while True:
            while temp:
                stack.append(temp)
                temp = temp.left
            curr = stack.pop()
            k -= 1
            if not k:
                return curr.val
            if curr.right:
                temp = curr.right