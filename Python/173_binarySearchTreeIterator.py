'''Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.arr = list()
        self._iterate(root)
        self.n = len(self.arr)
        self.i = 0

    def _iterate(self, node):
        stack = list()
        while stack or node:
            while node and node.left:
                stack.append(node)
                node = node.left
            if not node:
                node = stack.pop()
            self.arr.append(node.val)

            if node.right:
                node = node.right
            else:
                node = None

    def next(self) -> int:
        """
        @return the next smallest number
        """
        curr = self.arr[self.i]
        self.i += 1
        return curr

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return True if self.i < self.n else False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()