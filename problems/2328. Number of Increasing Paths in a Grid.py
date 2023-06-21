# link: https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

from functools import cache
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @cache
        def dfs(row, col) -> int:
            paths = 1
            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] > grid[row][col]:
                    paths += dfs(nr, nc)

            return paths % (10**9 + 7)

        result = 0
        for row in range(m):
            for col in range(n):
                result += dfs(row, col)
                result %= (10**9 + 7)

        return result

