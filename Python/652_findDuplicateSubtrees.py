'''Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return
the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def _iterate(node):
            if not node:
                return '#'
            string = str(node.val) + _iterate(node.left) + _iterate(node.right)
            self.dict[string].append(node)
            return string

        self.dict = collections.defaultdict(list)
        _iterate(root)
        result = list()
        for each in self.dict:
            if len(self.dict[each]) > 1:
                result.append(self.dict[each][0])

        return result