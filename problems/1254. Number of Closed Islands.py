# link: https://leetcode.com/problems/number-of-closed-islands/

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        def dfs1(row: int, col: int):
            if row < 0 or row >= ROW or col < 0 or col >= COL:
                return
            if grid[row][col] == 1:
                return

            grid[row][col] = 1
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for d_row, d_col in dirs:
                n_row, n_col = row + d_row, col + d_col
                dfs1(n_row, n_col)


        def dfs2(row: int, col: int) -> bool:
            if row < 0 or row >= ROW or col < 0 or col >= COL:
                return False
            if grid[row][col] == 1:
                return True

            grid[row][col] = 1
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for d_row, d_col in dirs:
                n_row, n_col = row + d_row, col + d_col
                if not dfs2(n_row, n_col):
                    return False
            return True

        for row in range(ROW):
            dfs1(row, 0)
            dfs1(row, COL-1)
        for col in range(COL):
            dfs1(0, col)
            dfs1(ROW-1, col)

        count = 0
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1:
                    continue
                if dfs2(row, col):
                    # print(row, col)
                    count += 1

        return count

