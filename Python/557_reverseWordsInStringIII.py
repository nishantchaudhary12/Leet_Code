'''Given a string, you need to reverse the order of characters in each word within a sentence while still preserving
whitespace and initial word order.'''


class Solution:
    def reverseWords(self, s: str) -> str:
        result = ''
        s = s.split(' ')
        for each in s:
            result += each[::-1] + ' '

        return result.rstrip(' ')