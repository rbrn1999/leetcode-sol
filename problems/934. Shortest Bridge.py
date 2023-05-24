import collections
class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
                return
            grid[i][j] = -1
            for dx, dy in dirs:
                dfs(i+dx, j+dy)
        
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    dfs(row, col)
                    break
            if grid[row][col] == -1:
                break

        q = collections.deque()
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    q.append((row, col))
        

        distance = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dx, dy in dirs:
                    n_row, n_col = row + dx, col + dy
                    if n_row < 0 or n_row >= n or n_col < 0 or n_col >= n or grid[n_row][n_col] == 1:
                        continue
                    if grid[n_row][n_col] == -1:
                        return distance
                    grid[n_row][n_col] = 1
                    q.append((n_row, n_col))
            distance += 1
        
        return -1
