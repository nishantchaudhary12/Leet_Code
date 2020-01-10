'''Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.'''


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        stack = [-1]
        for i, each in enumerate(s):
            if each == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    ans = max(ans, i - stack[-1])
                else:
                    stack.append(i)
        return ans