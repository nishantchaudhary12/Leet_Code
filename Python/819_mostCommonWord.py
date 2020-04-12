'''Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.
It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.
Words in the paragraph are not case sensitive.  The answer is in lowercase.'''


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punctuations = '''!?',;.'''
        for each in paragraph:
            if each in punctuations:
                paragraph = paragraph.replace(each, ' ')
        words = dict()
        banned = set(banned)
        paragraph = paragraph.split(' ')
        for each in paragraph:
            if each:
                each = each.lower()
                if each not in banned and each in words:
                    words[each] += 1
                elif each not in banned and each not in words:
                    words[each] = 1

        result = sorted(words.items(), key=lambda x: x[1])[-1][0]
        return result
