'''Given two lists Aand B, and B is an anagram of A. B is an anagram of A means B is made by randomizing the order of the elements in A.

We want to find an index mapping P, from A to B. A mapping P[i] = j means the ith element in A appears in B at index j.

These lists A and B may contain duplicates. If there are multiple answers, output any of them.'''


class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        indx = dict()
        for i, x in enumerate(B):
            if x not in indx:
                indx[x] = [i]
            else:
                indx[x].append(i)
        for i, each in enumerate(A):
            A[i] = indx[each].pop()
        return A
