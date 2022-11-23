# link: https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/submissions/

from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        q = deque()
        q.append(entrance)
        visited = set()
        visited.add((entrance[0], entrance[1]))
        steps = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if (r == 0 or c == 0 or r == m-1 or c == n-1) and (r, c) != (entrance[0], entrance[1]):
                    return steps
                dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in dirs:
                    nR, nC = r + dr, c + dc
                    if nR in range(m) and nC in range(n) and maze[nR][nC] == '.' and (nR, nC) not in visited:
                        visited.add((nR, nC))
                        q.append((nR, nC))
            steps += 1
        
        return -1
        