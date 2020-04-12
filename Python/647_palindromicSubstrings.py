'''Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.'''


class Solution:
    def countSubstrings(self, s: str) -> int:
        def count(left, right):
            currCount = 0
            n = len(s)
            while left >= 0 and right < n and s[left] == s[right]:
                currCount += 1
                left -= 1
                right += 1
            return currCount

        countPalindrome = 0
        for i in range(len(s)):
            countPalindrome += count(i, i)
            countPalindrome += count(i, i + 1)
        return countPalindrome
