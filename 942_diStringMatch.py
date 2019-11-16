'''Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]'''


class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        result_list = list()
        small = 0
        large = len(S)
        for char in S:
            if char == 'I':
                result_list.append(small)
                small += 1
            else:
                result_list.append(large)
                large -= 1
        result_list.append(large)
        return result_list