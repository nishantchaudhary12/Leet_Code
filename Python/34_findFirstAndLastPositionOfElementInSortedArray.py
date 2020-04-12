'''Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # if not nums: return [-1, -1]
        start = -1
        end = -1
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i + j)//2
            if nums[mid] == target:
                temp = mid
                while temp - 1 >= 0 and nums[temp - 1] == target:
                    temp = temp - 1
                start = temp
                temp = mid
                while temp + 1 < len(nums) and nums[temp + 1] == target:
                    temp = temp + 1
                end = temp
                break
            elif target > nums[mid]:
                i = mid + 1
            elif target < nums[mid]:
                j = mid - 1

        # print(start,end)
        return [start, end]