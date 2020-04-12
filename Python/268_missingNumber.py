'''Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        for i in range(len(nums)+1):
            if i not in nums:
                return i