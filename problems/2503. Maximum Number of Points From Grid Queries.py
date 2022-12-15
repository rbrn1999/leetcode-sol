# link: https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

import heapq
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        def dfs(q, r=0, c=0):
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            count = 1
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n or (nr, nc) in visited:
                    continue
                if (nr, nc) in edges_set:
                    continue
                if q <= grid[nr][nc]:
                    heapq.heappush(edges, (grid[nr][nc], nr, nc))
                    edges_set.add((nr, nc))
                    continue
                visited.add((nr, nc))
                count += dfs(q, nr, nc)

            return count

        result = [0] * len(queries)
        pos = [(q, i) for i, q in enumerate(queries)]
        pos.sort()
        visited = set()
        edges = [(grid[0][0], 0, 0)]
        edges_set = set() # to avoid additional node being added to edges(heap)
        edges_set.add((0, 0))
        points = 0
        for q, i in pos:
            for _ in range(len(edges)):
                val, r, c = edges[0]
                if q > val and (r, c) not in visited:
                    heapq.heappop(edges)
                    edges_set.remove((r, c))
                    visited.add((r, c))
                    points += dfs(q, r, c)
                else:
                    break
            result[i] = points

        return result
