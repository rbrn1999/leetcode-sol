# link: https://leetcode.com/problems/find-the-safest-path-in-a-grid/

# Dijkstra's
import itertools
import heapq
from collections import deque
class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def dfs(row: int, col: int, safeness: int, visited: set) -> bool:
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] <= safeness or (row, col) in visited:
                return False

            if row == m-1 and col == n-1:
                return True

            visited.add((row, col))

            for dr, dc in dirs:
                nr, nc = row+dr, col+dc
                if dfs(nr, nc, safeness, visited):
                    return True

            visited.remove((row, col))
            return False

        unsafe_q = deque()
        for row, col in itertools.product(range(m), range(n)):
            if grid[row][col] == 1:
                unsafe_q.append((row, col))

        safeness = 1

        while unsafe_q:
            safeness += 1
            for _ in range(len(unsafe_q)):
                row, col = unsafe_q.popleft()
                for dr, dc in dirs:
                    nr, nc = row+dr, col+dc
                    if nr >= 0 and nr < m and\
                        nc >= 0 and nc < n and \
                        grid[nr][nc] == 0:
                        grid[nr][nc] = safeness
                        unsafe_q.append((nr, nc))

        maxHeap = [(-(grid[0][0]-1), 0, 0)] # [-safeness, row, col]
        visited = set()

        while maxHeap:
            safeness, row, col = heapq.heappop(maxHeap)
            safeness = -safeness
            if (row, col) in visited:
                continue
            if row == m-1 and col == n-1:
                return safeness

            visited.add((row, col))

            for dr, dc in dirs:
                nr, nc = row+dr, col+dc
                if nr >= 0 and nr < m and \
                    nc >= 0 and nc < n and \
                    (nr, nc) not in visited:
                    minSafeness = min(safeness, grid[nr][nc]-1)
                    heapq.heappush(maxHeap, (-minSafeness, nr, nc))

        return -1

# BFS + Binary Search
import itertools
from collections import deque
class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def bfs(safeness: int) -> bool:
            if grid[0][0] <= safeness:
                return False

            visited = set()
            q = deque()
            q.append((0, 0))
            visited.add((0, 0))

            while q:
                row, col = q.popleft()
                if row == m-1 and col == n-1:
                    return True
                for dr, dc in dirs:
                    nr, nc = row+dr, col+dc
                    if nr >= 0 and nr < m and\
                        nc >= 0 and nc < n and \
                        grid[nr][nc] > safeness and \
                        (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))

            return False


        unsafe_q = deque()
        for row, col in itertools.product(range(m), range(n)):
            if grid[row][col] == 1:
                unsafe_q.append((row, col))

        safeness = 1

        while unsafe_q:
            safeness += 1
            for _ in range(len(unsafe_q)):
                row, col = unsafe_q.popleft()
                for dr, dc in dirs:
                    nr, nc = row+dr, col+dc
                    if nr >= 0 and nr < m and\
                        nc >= 0 and nc < n and \
                        grid[nr][nc] == 0:
                        grid[nr][nc] = safeness
                        unsafe_q.append((nr, nc))

        low = 0
        high = safeness
        while low < high:
            mid = (low + high + 1) // 2
            if bfs(mid):
                low = mid
            else:
                high = mid - 1

        return low
