'''Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all
strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.'''

from collections import Counter

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        first = [x for x in A[0]]
        result = list()
        dictCount = dict()
        for i in range(1, len(A)):
            dictCount[A[i]] = Counter(A[i])
        flag = False
        for i in first:
            for each in dictCount.keys():
                if i in dictCount[each]:
                    flag = True
                    dictCount[each][i] -= 1
                    if dictCount[each][i] == 0:
                        del dictCount[each][i]
                else:
                    flag = False
                    break
            if flag:
                result.append(i)
        return result