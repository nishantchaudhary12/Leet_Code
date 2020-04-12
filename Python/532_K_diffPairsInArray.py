'''Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array.
Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.'''

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        targetDict = dict()
        count = 0
        if k >= 0:
            for each in nums:
                targetDict[each] = targetDict[each] + 1 if each in targetDict else 1
            for each in targetDict:
                if k != 0 and each - k in targetDict and targetDict[each] > 0:
                    count += 1
                elif k == 0 and targetDict[each] > 1:
                    count += 1

        return count