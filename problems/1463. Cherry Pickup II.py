# link: https://leetcode.com/problems/cherry-pickup-ii/

from functools import cache
from itertools import product
class Solution:
    # Top-Down
    def cherryPickup(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @cache
        def dfs(r, c1, c2):
            if r == m or c1 < 0 or c1 >= n or c2 < 0 or c2 >= n:
                return 0

            val = grid[r][c1] + grid[r][c2]

            next_val = 0
            for nc1 in range(c1-1, c1+2):
                for nc2 in range(c2-1, c2+2):
                    if nc1 == nc2: # answer is not optimal
                        continue
                    next_val = max(next_val, dfs(r+1, nc1, nc2))

            return val + next_val
        
        return dfs(0, 0, n-1)

    # Bottom-Up
    def cherryPickup(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(n)]

        for r in reversed(range(m)):
            cur_dp = [[0] * n for _ in range(n)]
            for c1 in range(n-1):
                for c2 in range(c1+1, n):
                    max_cherries = 0
                    cherries = grid[r][c1] + grid[r][c2]
                    for c1_d, c2_d in product([-1, 0, 1], [-1, 0, 1]):
                        nc1, nc2 = c1 + c1_d, c2 + c2_d
                        if nc1 < 0 or nc2 == n:
                            continue
                        max_cherries = max(max_cherries, cherries + dp[nc1][nc2])
                    cur_dp[c1][c2] = max_cherries
            dp = cur_dp
        
        return dp[0][n-1]