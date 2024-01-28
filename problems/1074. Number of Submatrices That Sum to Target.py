# link: https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        prefix = [[0] * (n+1) for _ in range(m+1)]

        for row in range(m):
            for col in range(n):
                prefix[row+1][col+1] = prefix[row+1][col] + prefix[row][col+1] - prefix[row][col] + matrix[row][col]
        
        result = 0

        for r1 in range(m):
            for r2 in range(r1, m):
                count = {0: 1} # prefix_sum -> count
                for c in range(n):
                    cur_sum = prefix[r2+1][c+1] - prefix[r1][c+1]
                    diff = cur_sum - target
                    result += count.get(diff, 0)
                    count[cur_sum] = count.get(cur_sum, 0) + 1
        
        return result