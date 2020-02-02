'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.'''


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def generate(s, left, right):
            if len(s) == 2 * n:
                result.append(s)
            if left < n:
                generate(s + '(', left + 1, right)
            if right < left:
                generate(s + ')', left, right + 1)

        result = list()
        s = ''
        left = 0
        right = 0
        generate(s, left, right)

        return result