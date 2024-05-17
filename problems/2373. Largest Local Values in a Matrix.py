# link: https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        result = [[0] * (n-2) for _ in range(n-2)]
        for row in range(n-2):
            for col in range(n-2):
                for i in range(row, row+3):
                    for j in range(col, col+3):
                        result[row][col] = max(result[row][col], grid[i][j])
        
        return result