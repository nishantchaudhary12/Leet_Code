'''Given an array of integers arr, write a function that returns true if and only if the number of occurrences of
each value in the array is unique.'''


from collections import Counter

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        uniqueDict = Counter(arr)
        unique = set()
        for i, x in uniqueDict.items():
            if x in unique:
                return False
            unique.add(x)
        return True