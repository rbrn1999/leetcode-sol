# link: https://leetcode.com/problems/shortest-path-in-binary-matrix/

from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        q = deque()
        q.append((0, 0))
        grid[0][0] = 1 # mark visited in place, could use a hash set instead
        steps = 1

        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if (i, j) == (n-1, n-1):
                    return steps
                for new_i in range(i-1, i+2):
                    for new_j in range(j-1, j+2):
                        if new_i < 0 or new_i >= n or new_j < 0 or new_j >= n or grid[new_i][new_j] == 1:
                            continue
                        q.append((new_i, new_j))
                        grid[new_i][new_j] = 1

            steps += 1
            
        return -1
        