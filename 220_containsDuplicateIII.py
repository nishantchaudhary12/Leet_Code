'''Given an array of integers, find out whether there are two distinct indices i and j in the array such that the
absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.'''


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0: return False
        data = dict()
        w = t + 1  #to take care of division by zero
        for i, each in enumerate(nums):
            curr = each // w
            if curr in data:
                return True
            if curr - 1 in data and abs(each - data[curr - 1]) < w:  #less than to cancel + 1
                return True
            if curr + 1 in data and abs(each - data[curr + 1]) < w:
                return True
            data[curr] = each
            if i >= k :
                del data[nums[i - k] // w]
        return False