'''Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.'''


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = list()
        for each in nums:
            if nums[abs(each) - 1] > 0:
                nums[abs(each) - 1] *= -1
        for i, each in enumerate(nums):
            if each > 0:
                result.append(i + 1)
        return result