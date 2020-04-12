'''Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right,
then right to left for the next level and alternate between).'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def _iterate(node, d):
            if len(result) - 1 < d:
                result.append([node.val])
            else:
                result[d].append(node.val)

            if node.left:
                _iterate(node.left, d + 1)
            if node.right:
                _iterate(node.right, d + 1)

        if not root: return []
        result = list()
        _iterate(root, 0)
        print(result)
        for i in range(len(result)):
            if i % 2 != 0:
                result[i] = result[i][::-1]
        return result