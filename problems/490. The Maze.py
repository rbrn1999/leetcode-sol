# link: https://leetcode.com/problems/the-maze/

class Solution:
    def hasPath(self, maze: list[list[int]], start: list[int], destination: list[int]) -> bool:
        m, n = len(maze), len(maze[0])
        dirs = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        def dfs(row: int, col: int, visited: set) -> bool:
            if (row, col) in visited:
                return False
            if [row, col] == destination:
                return True
            
            visited.add((row, col))

            for dr, dc in dirs:
                r, c = row, col
                while r >= 0 and r < m and c >= 0 and c < n and maze[r][c] == 0:
                    r += dr
                    c += dc
                r -= dr
                c -= dc
                if dfs(r, c, visited):
                    return True
            
            return False
        
        return dfs(start[0], start[1], set())