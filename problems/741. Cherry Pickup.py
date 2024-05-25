# link: https://leetcode.com/problems/cherry-pickup/

from functools import cache
class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        @cache
        def dfs(r1: int, c1: int, r2: int) -> int:
            c2 = r1 + c1 - r2
            if r1 == n-1 and c1 == n-1 and r2 == n-1 and c2 == n-1:
                return grid[n-1][n-1]
            
            if r1 == n or c1 == n or r2 == n or c2 == n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -float('inf')
            
            
            dirs = [(1, 0), (0, 1)]

            cherries = grid[r1][c1]
            more_cherries = -float('inf')
            if (r2, c2) != (r1, c1):
                cherries += grid[r2][c2]
            for dr1, dc1 in dirs:
                nr1, nc1 = r1 + dr1, c1 + dc1
                for dr2, dc2 in dirs:
                    nr2 = r2 + dr2
                    more_cherries = max(more_cherries, dfs(nr1, nc1, nr2))
            
            return cherries + more_cherries
        
        return max(dfs(0, 0, 0), 0)


