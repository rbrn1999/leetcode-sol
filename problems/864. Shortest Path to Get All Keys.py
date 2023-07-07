# link: https://leetcode.com/problems/shortest-path-to-get-all-keys/

from collections import deque
class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        m, n = len(grid), len(grid[0])
        keyList = list(set([c.lower() for row in grid for c in row if c.isalpha()]))
        keyMap = {key: i for i, key in enumerate(keyList)}
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set() # key = (row, col, key_mask)
        q = deque()

        for row in range(m):
            for col in range(n):
                if grid[row][col] == '@':
                    start = (row, col)
                    break

        q.append((*start, tuple([0] * len(keyList))))

        steps = 0
        while q:
            for _ in range(len(q)):
                row, col, key_mask = q.popleft()
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] == '#':
                        continue
                    if grid[nr][nc].isalpha() and grid[nr][nc].isupper() and key_mask[keyMap[grid[nr][nc].lower()]] == 0:
                        continue
                    new_key_mask = list(key_mask)
                    if grid[nr][nc] in keyMap:
                        new_key_mask[keyMap[grid[nr][nc]]] = 1
                    new_key_mask = tuple(new_key_mask)
                    if all(new_key_mask):
                        return steps + 1
                    if (nr, nc, new_key_mask) not in visited:
                        q.append((nr, nc, new_key_mask))
                        visited.add((nr, nc, new_key_mask))
            steps += 1

        return -1

