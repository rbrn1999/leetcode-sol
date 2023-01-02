# link: https://leetcode.com/problems/rotting-oranges/

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        rottens = deque()
        freshes = set()

        def spread(row, col):
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            rottens = []
            for d_row, d_col in dirs:
                n_row = row + d_row
                n_col = col + d_col
                if n_row < 0 or n_col < 0 or n_row >=ROWS or n_col >= COLS or grid[n_row][n_col] != 1:
                    continue
                grid[n_row][n_col] = 2
                rottens.append((n_row, n_col))
                freshes.remove((n_row, n_col))
            return rottens

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    rottens.append((row, col))
                elif grid[row][col] == 1:
                    freshes.add((row, col))
        minute = 0
        while rottens and freshes:
            for _ in range(len(rottens)):
                row, col = rottens.popleft()
                rottens.extend(spread(row, col))
            minute += 1

        return minute if not freshes else -1
