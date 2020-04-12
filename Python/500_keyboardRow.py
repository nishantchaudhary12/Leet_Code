'''Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.'''

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p')
        row2 = ('a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l')
        row3 = ('z', 'x', 'c', 'v', 'b', 'n', 'm')
        result = list()
        for each in words:
            flag = True
            if each[0].lower() in row1:
                row = row1
            elif each[0].lower() in row2:
                row = row2
            else:
                row = row3
            for i in each:
                if i.lower() not in row:
                    flag = False
                    break
            if flag:
                result.append(each)
        return result