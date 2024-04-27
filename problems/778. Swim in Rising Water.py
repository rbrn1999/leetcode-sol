# link: https://leetcode.com/problems/swim-in-rising-water/

import heapq
class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        minHeap = [(grid[0][0], 0, 0)] # (time, row, col)

        visited = set([(0, 0)])
        while minHeap:
            t, row, col = heapq.heappop(minHeap)
            if (row, col) == (n-1, n-1):
                return t

            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if (nr, nc) in visited or nr < 0 or nr >= n or nc < 0 or nc >= n:
                    continue
                else:
                    visited.add((nr, nc))
                new_t = max(t, grid[nr][nc])
                heapq.heappush(minHeap, (new_t, nr, nc))

        return -1