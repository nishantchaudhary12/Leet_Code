'''Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.'''


class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        n = len(height)
        i = 0
        j = n - 1
        while i < j:
            currA = min(height[i], height[j]) * (j - i)
            area = max(area, currA)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return area
