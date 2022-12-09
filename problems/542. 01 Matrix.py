# link: https://leetcode.com/problems/01-matrix/

from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        result = [[float('inf')] * n for _ in range(m)]



        q = deque()
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
        steps = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                if steps >= result[row][col]:
                    continue

                result[row][col] = steps
                dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                for d_r, d_c in dirs:
                    nR, nC = row + d_r, col + d_c
                    if nR in range(m) and nC in range(n) and mat[nR][nC] == 1 and steps + 1 < result[nR][nC]:
                        q.append((nR, nC))

            steps += 1
        return result



