# link: https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for row in range(m):
            col = 0
            offset = 0
            num = matrix[row+offset][col+offset]
            offset += 1
            while row + offset < m and col + offset < n:
                if matrix[row+offset][col+offset] != num:
                    return False
                offset += 1
            
        for col in range(1, n):
            row = 0
            offset = 0
            num = matrix[row+offset][col+offset]
            offset += 1
            while row + offset < m and col + offset < n:
                if matrix[row+offset][col+offset] != num:
                    return False
                offset += 1  
        
        return True