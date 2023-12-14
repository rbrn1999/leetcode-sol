# link: https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        diff = [[0] * n for _ in range(m)]
        for row in range(m):
            val = sum(grid[row][col] if grid[row][col] == 1 else -1 for col in range(n))
            for col in range(n):
                diff[row][col] += val
        for col in range(n):
            val = sum(grid[row][col] if grid[row][col] == 1 else -1 for row in range(m))
            for row in range(m):
                diff[row][col] += val
        
        return diff
