# link: https://leetcode.com/problems/score-after-flipping-matrix/

class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # The first bit should be 1 (flip the row if not)
        result = m * (2 ** (n-1))

        for col in range(1, n):
            ones = 0
            for row in range(m):
                if grid[row][0] ^ grid[row][col] == 1: # if first bit is 0, we had flipped this row
                    ones += 1

            zeros = m - ones
            if zeros > ones:
                ones, zeros = zeros, ones

            result += ones * (2 ** (n-1-col))

        return result
