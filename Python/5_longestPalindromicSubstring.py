'''Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(string, start, end):
            while start >= 0 and end < len(string) and string[start] == string[end]:
                start -= 1
                end += 1
            return end - 1 - start

        if not s:
            return ''
        start = 0
        end = 0
        for i in range(len(s) - 1):
            len1 = check(s, i, i)
            len2 = check(s, i, i + 1)
            length = max(len1, len2)
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
                # print(start, end)

        return s[start:end + 1]
