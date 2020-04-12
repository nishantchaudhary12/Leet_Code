'''Given two arrays, write a function to compute their intersection.'''

from collections import Counter


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1 = set(nums1)
        num2 = Counter(nums2)
        result = list()
        for each in num1:
            if each in num2.keys() and num2[each] > 0:
                result.append(each)
                num2[each] = 0
        return result
