#two sum
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        temp = {}
        for index, elem in enumerate(nums):
            if elem in temp:
                return [temp[elem], index]
            else:
                temp[target - elem] = index
