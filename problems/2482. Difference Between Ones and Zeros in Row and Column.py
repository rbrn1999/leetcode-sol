# link: https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        diff = [[float('inf')] * n for _ in range(m)]
        rows = [sum(grid[i]) for i in range(m)]
        cols = [sum([grid[r][c] for r in range(m)]) for c in range(n)]

        for r in range(m):
            for c in range(n):
                diff[r][c] = 2 * (rows[r] + cols[c]) - m - n

        return diff
