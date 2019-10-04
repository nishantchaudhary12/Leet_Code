'''Given an integer array, find three numbers whose product is maximum and output the maximum product.'''

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max((nums[-1] * nums[-2] * nums[-3]), (nums[-1] * nums[0] * nums[1]))
