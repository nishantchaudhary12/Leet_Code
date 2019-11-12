'''Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import deque

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        flag = 0
        queue = deque([root, flag])
        maxSum = 0
        currSum = 0
        maxLevel = 1
        currLevel = 1
        while len(queue) > 1:
            elem = queue.popleft()
            if elem != flag:
                currSum += elem.val
                if elem.left:
                    queue.append(elem.left)
                if elem.right:
                    queue.append(elem.right)
            else:
                if currSum > maxSum:
                    maxSum = currSum
                    maxLevel = currLevel
                currSum = 0
                currLevel += 1
                queue.append(flag)
        return maxLevel