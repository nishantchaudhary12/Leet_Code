'''Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxLimit = 0
        n = len(nums)
        for i, each in enumerate(nums):
            if maxLimit < i:
                return False
            if maxLimit >= n-1:
                return True
            maxLimit = max(maxLimit, i + each)