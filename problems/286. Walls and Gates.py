# link: https://leetcode.com/problems/walls-and-gates/

from collections import deque
class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        q = deque()
        for row in range(m):
            for col in range(n):
                if rooms[row][col] == 0:
                    q.append((row, col))
        
        distance = 1
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n or rooms[nr][nc] == -1 or rooms[nr][nc] <= distance:
                        continue
                    rooms[nr][nc] = distance
                    q.append((nr, nc))
            distance += 1
        
        return