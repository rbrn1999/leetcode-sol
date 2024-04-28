# link: https://leetcode.com/problems/right-triangles/

from collections import defaultdict
class Solution:
    def numberOfRightTriangles(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_map = defaultdict(int)
        col_map = defaultdict(int)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    row_map[r] += 1
                    col_map[c] += 1

        result = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    result += (row_map[r]-1) * (col_map[c]-1)

        return result
