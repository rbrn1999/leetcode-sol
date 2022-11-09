# link: https://leetcode.com/problems/number-of-islands/

# DFS solution
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def sink_island(row, col):
            if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] == '0':
                return
            grid[row][col] = '0'
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            for d_row, d_col in directions:
                sink_island(row+d_row, col+d_col)
        
        res = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    res += 1
                    sink_island(row, col)
        return res

# BFS solution

from collections import deque
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def sink_island(row, col):
            q = deque()
            q.append((row, col))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while q:
                row, col = q.popleft()
                for off_r, off_c in directions:
                    r = row + off_r
                    c = col + off_c
                    if r in range(m) and c in range(n) and grid[r][c] == '1':
                        grid[r][c] = '0'
                        q.append((r, c))
        
        res = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    grid[row][col] = '0'
                    res += 1
                    sink_island(row, col)
        return res
        