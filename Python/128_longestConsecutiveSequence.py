'''Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = set(nums)
        longest = 1
        while nums:
            curr = 1
            i = j = nums.pop()
            while i - 1 in nums:
                nums.remove(i-1)
                i -= 1
                curr += 1
            while j + 1 in nums:
                nums.remove(j+1)
                j += 1
                curr += 1
            longest = max(longest, curr)
        return longest