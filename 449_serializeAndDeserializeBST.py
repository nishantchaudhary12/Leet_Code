'''Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored
in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized
to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root: return ''
        stack = [root]
        res = list()
        while stack:
            root = stack.pop()
            res.append(str(root.val))
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

        return ','.join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data: return None
        data = [int(i) for i in data.split(',')]
        node = TreeNode(data[0])
        temp = node
        stack = list()
        for i in data[1:]:
            if i < temp.val:
                temp.left = TreeNode(i)
                stack.append(temp)
                temp = temp.left
            else:
                while stack and stack[-1].val < i:
                    temp = stack.pop()
                temp.right = TreeNode(i)
                temp = temp.right
        return node

    # Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))