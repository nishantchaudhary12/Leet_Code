'''Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.'''


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.islower():
            return True
        elif word.isupper():
            return True
        else:
            if word[0].isupper():
                word = word[1:]
                if word.islower():
                    return True
                return False