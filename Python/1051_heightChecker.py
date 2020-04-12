'''
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students not standing in the right positions.
(This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)'''


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if new[i] != heights[i]:
                count += 1
        return count