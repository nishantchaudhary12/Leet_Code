'''Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.'''


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[0] > target:
            return 0
        elif nums[-1] < target:
            return len(nums)
        else:
            for i in range(len(nums)):
                if nums[i] >= target:
                    return i
                

        