'''Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.'''


class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        currentMax = 0
        prevMax = 0
        for i in range(len(nums) - 1):
            currentMax = max(currentMax, nums[i] + i)
            if i == prevMax:
                jump += 1
                prevMax = currentMax
        return jump
