'''Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.'''


class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A.sort()
        result = [0 for i in range(len(A))]
        i = 0
        j = 1
        for each in A:
            if each % 2 == 0:
                result[i] = each
                i += 2
            else:
                result[j] = each
                j += 2
        return result