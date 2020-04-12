'''Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes
the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.'''


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[2 ** 31 - 1 for j in range(n)]for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j > 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif j == 0 and i > 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                elif i != 0 and j != 0:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
                else:
                    dp[i][j] = grid[i][j]
        return dp[-1][-1]
