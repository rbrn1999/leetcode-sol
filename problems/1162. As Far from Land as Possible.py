# link: https://leetcode.com/problems/as-far-from-land-as-possible

from collections import deque

class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        n = len(grid)
        distance = 0
        max_d = -1
        q = deque([(row, col) for col in range(n) for row in range(n)if grid[row][col] == 1])
        visited = set()
        # backtrack from every island to water with breadth first search
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for d_r, d_c in dirs:
                    nR, nC = row + d_r, col + d_c
                    if 0 <= nR < n and 0 <= nC < n and (nR, nC) not in visited and grid[nR][nC] == 0:
                        max_d = distance + 1
                        visited.add((nR, nC))
                        q.append((nR, nC))
            distance += 1

        return max_d 
