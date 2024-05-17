# link: https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

# 0-1 BFS
from collections import deque
class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        steps = 0
        q = deque()
        visited = set()
        q.append((0, 0))
        visited.add((0, 0))
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while q:
            next_q = deque()
            while q:
                r, c = q.popleft()
                if r == m-1 and c == n-1:
                    return steps
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if (nr, nc) in visited or nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    visited.add((nr, nc))
                    if grid[nr][nc] == 0:
                        q.append((nr, nc))
                    else:
                        next_q.append((nr, nc))

            q = next_q
            steps += 1

        return steps

# Dijkstra's

import heapq
class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        heap = [(0, 0, 0)]
        visited = set()
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while heap:
            removes, r, c = heapq.heappop(heap)
            if (r, c) in visited:
                continue
            else:
                visited.add((r, c))

            if r == m-1 and c == n-1:
                return removes

            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if (nr, nc) in visited or nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                heapq.heappush(heap, (removes + grid[nr][nc], nr, nc))

        return -1
