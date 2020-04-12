'''Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.'''

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        length = len(arr)
        while i < length:
            if arr[i] == 0:
                arr.insert(i+1, 0)
                i += 1
            i += 1
            while len(arr) > length:
                del arr[-1]