# link: https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [list(row) for row in zip(*A)]
#         m = len(matrix)
#         n = len(matrix[0])
#         t = [[0]*m for _ in range(n)]

#         for i in range(m):
#             for j in range(n):
#                 t[j][i] = matrix[i][j]

#         return t
