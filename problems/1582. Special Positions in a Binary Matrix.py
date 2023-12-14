# link: https://leetcode.com/problems/special-positions-in-a-binary-matrix/

class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_ones = [0] * m
        col_ones = [0] * n
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1:
                    row_ones[row] += 1
                    col_ones[col] += 1
        
        count = 0
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1 and row_ones[row] == 1 and col_ones[col] == 1:
                    count += 1
        
        return count