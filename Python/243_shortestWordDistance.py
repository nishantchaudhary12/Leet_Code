'''Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.'''


class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        d = 2 ** 31 - 1
        indx1, indx2 = -1, -1
        for i, each in enumerate(words):
            if each == word1:
                indx1 = i
            elif each == word2:
                indx2 = i
            if indx1 >= 0 and indx2 >= 0:
                d = min(d, abs(indx1 - indx2))

        return d