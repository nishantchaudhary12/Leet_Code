'''Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)

        for i in range(m - n + 1):
            if haystack[i:i+n] == needle:
                return i
        return -1