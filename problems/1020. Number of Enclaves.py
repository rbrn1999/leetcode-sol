# link: https://leetcode.com/problems/number-of-enclaves/

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        def dfs(row: int, col: int):
            if row < 0 or row >= ROW or col < 0 or col >= COL or grid[row][col] == 0:
                return
            grid[row][col] = 0
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for d_row, d_col in dirs:
                dfs(row+d_row, col+d_col)

        for row in range(ROW):
            dfs(row, 0)
            dfs(row, COL-1)
        for col in range(COL):
            dfs(0, col)
            dfs(ROW-1, col)

        count = 0
        for row in grid:
            for element in row:
                if element == 1:
                    count += 1

        return count

