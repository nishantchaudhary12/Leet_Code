'''Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        pairs = {')': '(', '}': '{', ']': '['}
        for each in s:
            if each in ('(', '{', '['):
                stack.append(each)
            else:
                if stack:
                    if pairs[each] != stack.pop():
                        return False
                else:
                    return False
        return True if not stack else False
