'''Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root:
            que = Queue(maxsize=0)
            que.put((root, 1))
            while not que.empty():
                temp, level = que.get()
                if not temp.left and not temp.right:
                    return level
                if temp.left:
                    que.put((temp.left, level + 1))
                if temp.right:
                    que.put((temp.right, level + 1))
        return 0