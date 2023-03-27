# link: https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        if m >= n:
            dp = [[0]*n for _ in range(2)]
            preSum = 0
            for col in range(n):
                preSum += grid[0][col]
                dp[0][col] = preSum

            for row in range(1, m):
                dp[1][0] = dp[0][0] + grid[row][0]
                for col in range(1, n):
                    dp[1][col] = min(dp[1][col-1], dp[0][col]) + grid[row][col]
                dp = [dp[1], [0]*n]

            return dp[0][n-1]
        else:
            dp = [[0]*m for _ in range(2)]
            preSum = 0
            for row in range(m):
                preSum += grid[row][0]
                dp[0][row] = preSum

            for col in range(1, n):
                dp[1][0] = dp[0][0] + grid[0][col]
                for row in range(1, m):
                    dp[1][row] = min(dp[1][row-1], dp[0][row]) + grid[row][col]
                dp = [dp[1], [0]*m]

            return dp[0][m-1]

