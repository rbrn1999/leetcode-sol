# link: https://leetcode.com/problems/island-perimeter/

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        result = 0
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    continue
                for dx, dy in dirs:
                    nr, nc = r + dx, c + dy
                    if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] == 0:
                        result += 1

        return result
