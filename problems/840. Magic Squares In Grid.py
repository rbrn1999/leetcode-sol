# link: https://leetcode.com/problems/magic-squares-in-grid/

import itertools
class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        count = 0

        for r, c in itertools.product(range(ROW-2), range(COL-2)):
            if sum(grid[r][c:c+3]) != 15:
                continue
            if sum(grid[r+1][c:c+3]) != 15:
                continue
            if sum(grid[r+2][c:c+3]) != 15:
                continue

            valid = True
            for k in range(3):
                if grid[r+k][c] + grid[r+k][c+1] + grid[r+k][c+2] != 15:
                    valid = False
                    break
            if not valid:
                continue

            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15:
                continue

            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15:
                continue

            numbers = set(range(1, 10))
            for row, col in itertools.product(range(r+3), range(c+3)):
                if grid[row][col] not in numbers:
                    valid = False
                    break
                else:
                    numbers.remove(grid[row][col])

            if valid:
                count += 1

        return count
