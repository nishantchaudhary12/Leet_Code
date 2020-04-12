'''Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.'''


class Solution:
    def removeVowels(self, S: str) -> str:
        result = ''
        for i, x in enumerate(S):
            if x not in ('a', 'e', 'i', 'o', 'u'):
                result += S[i]
        return result
