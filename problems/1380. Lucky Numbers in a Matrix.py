# link: https://leetcode.com/problems/lucky-numbers-in-a-matrix/

# Simulation
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        result = []
        
        for row in range(m):
            min_col = 0
            for col in range(1, n):
                if matrix[row][col] < matrix[row][min_col]:
                    min_col = col

            if max(matrix[r][min_col] for r in range(m)) == matrix[row][min_col]:
                result.append(matrix[row][min_col])
        
        return result

# Greedy

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        row_min_max = -float('inf')
        col_max_min = float('inf')

        for row in range(m):
            row_min = min(matrix[row])
            row_min_max = max(row_min_max, row_min)
        
        for col in range(n):
            col_max = max(matrix[r][col] for r in range(m))
            col_max_min = min(col_max_min, col_max)
        
        if row_min_max == col_max_min:
            return [row_min_max]
        else:
            return []
