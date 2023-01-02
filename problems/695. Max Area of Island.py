# link: https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid) , len(grid[0])

        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROW or col >= COL or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            area = 1
            for d_row, d_col in dirs:
                area += dfs(row+d_row, col+d_col)
            return area

        result = 0
        for row in range(ROW):
            for col in range(COL):
                result = max(result, dfs(row, col))

        return result

