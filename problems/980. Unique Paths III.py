# link: https://leetcode.com/problems/unique-paths-iii/

class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        start = (-1, -1)
        end = (-1, -1)
        obstacles = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == -1:
                    obstacles += 1

        visited = set()
        def dfs(i, j):
            if i >= m or j >= n or i < 0 or j < 0 or \
            (i, j) in visited or grid[i][j] == -1:
                return 0
            if grid[i][j] == 2 :
                return 1 if len(visited) == m * n - (obstacles + 1) else 0

            visited.add((i, j))
            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            count = sum([dfs(i+di, j+dj) for di, dj in dirs])
            visited.remove((i, j))
            return count

        return dfs(start[0], start[1])
