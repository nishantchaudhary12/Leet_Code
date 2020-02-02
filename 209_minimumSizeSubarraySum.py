'''Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of
which the sum ≥ s. If there isn't one, return 0 instead.'''


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i = 0
        j = 0
        minLen = 2 ** 31 - 1
        currSum = 0
        while j < len(nums):
            currSum += nums[j]
            while currSum >= s:
                minLen = min(minLen, j - i + 1)
                currSum -= nums[i]
                i += 1
            j += 1
        return minLen if minLen != 2 ** 31 - 1 else 0

