'''Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.'''


class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        squares = list()
        for each in A:
            squares.append(each * each)
        squares.sort()
        return squares