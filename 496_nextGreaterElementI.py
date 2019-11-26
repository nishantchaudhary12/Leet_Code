'''You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist,
output -1 for this number.'''

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = list()
        indx = dict()
        n = len(nums2)
        for i, num in enumerate(nums2):
            indx[num] = i
        for each in nums1:
            i = indx[each]
            while i < n:
                if nums2[i] > each:
                    result.append(nums2[i])
                    break
                i += 1
            if i == len(nums2):
                result.append(-1)
        return result