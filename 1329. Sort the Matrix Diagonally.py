# link: https://leetcode.com/problems/sort-the-matrix-diagonally/

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        result = [[0]*n for _ in range(m)]
        val = []
        ind = []
        for i in range(m):
            cur_diag_val = []
            cur_diag_ind = []
            j = 0
            while i < m and j < n:
                cur_diag_val.append(mat[i][j])
                cur_diag_ind.append((i, j))

                i += 1
                j += 1
            val.append(cur_diag_val)
            ind.append(cur_diag_ind)

        for i in range(1, n):
            cur_diag_val = []
            cur_diag_ind = []
            j = 0
            while i < n and j < m:
                cur_diag_val.append(mat[j][i])
                cur_diag_ind.append((j, i))

                i += 1
                j += 1
            val.append(cur_diag_val)
            ind.append(cur_diag_ind)

        for i in range(len(val)):
            val[i].sort()
            for j in range(len(val[i])):
                result[ind[i][j][0]][ind[i][j][1]] = val[i][j]

        return result
