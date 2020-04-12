'''You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = 0

    def pathSum(self, root: TreeNode, sum: int) -> int:
        def _iterate(node, prevSum, target):
            if not node:
                return
            currSum = prevSum + node.val
            if currSum - target in cache:
                self.ans += cache[currSum - target]
            if currSum in cache:
                cache[currSum] += 1
            else:
                cache[currSum] = 1

            _iterate(node.left, currSum, sum)
            _iterate(node.right, currSum, sum)
            cache[currSum] -= 1

        cache = {0: 1}
        if root:
            _iterate(root, 0, sum)
        return self.ans
