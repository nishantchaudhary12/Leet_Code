'''Implement a trie with insert, search, and startsWith methods.'''


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = dict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.dict
        for each in word:
            if each not in curr:
                curr[each] = {}
            curr = curr[each]
        curr['#'] = word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.dict
        for each in word:
            if each not in curr:
                return False
            curr = curr[each]
        return True if '#' in curr else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.dict
        for each in prefix:
            if each not in curr:
                return False
            curr = curr[each]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)