# link: https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

class Solution:
    def maxMoves(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * m
        result = 0

        for col in range(1, n):
            next_dp = [-1000] * m
            for row in range(m):
                if row > 0 and grid[row][col] > grid[row-1][col-1]:
                    next_dp[row] = dp[row-1] + 1
                if grid[row][col] > grid[row][col-1]:
                    next_dp[row] = max(next_dp[row], dp[row] + 1)
                if row < m-1 and grid[row][col] > grid[row+1][col-1]:
                    next_dp[row] = max(next_dp[row], dp[row+1] + 1)
                result = max(result, next_dp[row])
            dp = next_dp
        
        return result