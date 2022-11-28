# link: https://leetcode.com/problems/path-with-minimum-effort
# solution reference: https://pythonalgos.com/dijkstras-algorithm-in-5-steps-with-python/

from heapq import heappop, heappush
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        def neighbors(x: int, y: int) -> list[(int, int, int)]: # [(distance, i, j)]
            res = []
            nonlocal rows, cols, dist
            if x > 0: res.append((max(abs(heights[x-1][y] - heights[x][y]), dist[x][y]), x-1, y))
            if x < rows-1: res.append((max(abs(heights[x+1][y] - heights[x][y]), dist[x][y]), x+1, y))
            if y > 0: res.append((max(abs(heights[x][y-1] - heights[x][y]), dist[x][y]), x, y-1))
            if y < cols-1: res.append((max(abs(heights[x][y+1] - heights[x][y]), dist[x][y]), x, y+1))
            return res

        rows, cols = len(heights), len(heights[0])
        dist = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        dist[0][0] = 0
        
        minHeap = [(0, 0, 0)] # (distance, i, j)
        
        while minHeap:
            _, u, r = heappop(minHeap)
            if visited[u][r]:
                continue
            else:
                visited[u][r] = True
            
            for d, x, y in neighbors(u, r):
                dist[x][y] = min(dist[x][y], d)
                heappush(minHeap, (dist[x][y], x, y))

        return dist[-1][-1]
