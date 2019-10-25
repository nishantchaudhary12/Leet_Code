'''There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.'''


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        curr_list = nums1 + nums2
        curr_list.sort()
        length = float(len(curr_list))
        if length % 2 != 0:
            median = (length / 2) + 0.5
            return curr_list[int(median)-1]
        else:
            median = float(curr_list[int(length) // 2] + curr_list[int(length) // 2 - 1])
            median /= 2
            return median