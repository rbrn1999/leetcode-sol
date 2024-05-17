# link: https://leetcode.com/problems/shortest-path-to-get-food/

import itertools
from collections import deque
class Solution:
    def getFood(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        row, col = -1, -1

        for r, c in itertools.product(range(m), range(n)):
            if grid[r][c] == '*':
                row, col = r, c
                break

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q = deque()
        visited = set()
        q.append((row, col))
        visited.add((row, col))

        steps = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] == 'X' or (nr, nc) in visited:
                        continue
                    if grid[nr][nc] == '#':
                        return steps + 1
                    q.append((nr, nc))
                    visited.add((nr, nc))

            steps += 1

        return -1
