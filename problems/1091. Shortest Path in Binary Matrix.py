# link: https://leetcode.com/problems/shortest-path-in-binary-matrix/
# solution reference: https://leetcode.com/problems/shortest-path-in-binary-matrix/discuss/312827/Python-Concise-BFS/744041

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [[1,0], [-1,0], [0,1], [0,-1], [-1,-1], [1,1], [1,-1], [-1,1]]
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        
        visited = set()
        queue = deque([(0, 0, 1)]) # indice, distance
        visited.add((0,0))
        
        while queue:
            i, j, dist = queue.popleft()
            if i == n-1 and j == n-1:
                return dist
            for d1, d2 in dirs:
                x, y = i+d1, j+d2
                if (0 <= x < n and 0 <= y < n) and ((x, y) not in visited) and grid[x][y] == 0:
                    visited.add((x, y))
                    queue.append((x, y, dist+1))
        return -1
        