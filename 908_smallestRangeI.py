'''Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.'''


class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A) > 1:
            min_value = min(A)
            max_value = max(A)
            min_value += K
            max_value -= K
            if max_value < min_value:
                return 0
            else:
                return max_value - min_value
        else:
            return 0
