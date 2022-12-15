# link: https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        for row in range(1, m):
            for col in range(n):
                prev = matrix[row-1][col]
                if col >= 1:
                    prev = min(prev, matrix[row-1][col-1])
                if col < n-1:
                    prev = min(prev, matrix[row-1][col+1])
                matrix[row][col] += prev

        return min(matrix[-1])
