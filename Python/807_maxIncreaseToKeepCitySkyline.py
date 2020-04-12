'''In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there.
We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings).
Height 0 is considered to be a building as well.

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right,
must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by
all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?'''


class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        numRows = len(grid)
        numColumns = len(grid[0])

        maxRow = [0] * numRows
        maxColumn = [0] * numRows
        for i in range(numRows):
            cr = 0
            for j in range(numColumns):
                cr = max(cr, grid[i][j])
                maxColumn[j] = max(maxColumn[j], grid[i][j])
            maxRow[i] = cr

        j = 0
        while j < numColumns:
            curr = list()
            for i in grid:
                curr.append(i[j])
            maxColumn.append(max(curr))
            j += 1

        count = 0
        for i in range(numRows):
            for j in range(numColumns):
                count += min(maxRow[i], maxColumn[j]) - grid[i][j]

        return count