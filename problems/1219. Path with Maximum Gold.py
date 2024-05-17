# link: https://leetcode.com/problems/path-with-maximum-gold/

class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(row: int, col: int, visited: set) -> int:
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0 or (row, col) in visited:
                return 0

            visited.add((row, col))
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            gold = grid[row][col]
            for dr, dc in dirs:
                nr, nc = row+dr, col+dc
                gold = max(gold, grid[row][col] + dfs(nr, nc, visited))

            visited.remove((row, col))
            return gold



        maxGold = 0
        for row in range(m):
            for col in range(n):
                maxGold = max(maxGold, dfs(row, col, set()))

        return maxGold
