# link: https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROW, COL = len(board), len(board[0])
        def dfs(row, col):
            if row<0 or col<0 or row>=ROW or col>=COL or board[row][col] != 'O':
                return
            board[row][col] = '_'
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for d_row, d_col in dirs:
                dfs(row+d_row, col+d_col)

        for col in range(COL):
            dfs(0, col)
            dfs(ROW-1, col)
        for row in range(ROW):
            dfs(row, 0)
            dfs(row, COL-1)

        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == '_':
                    board[row][col] = 'O'
                elif board[row][col] == 'O':
                    board[row][col] = 'X'
                else:
                    pass

