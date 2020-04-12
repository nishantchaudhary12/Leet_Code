'''Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        new = nums[::-1]
        maxP = max(nums[0], new[0])
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1
            new[i] *= new[i-1] or 1
            maxP = max(nums[i], new[i], maxP)
        return maxP