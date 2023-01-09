# link: https://leetcode.com/problems/battleships-in-a-board/

class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        ROWS, COLS = len(board), len(board[0])
        def dfs(row, col):
            if row >= ROWS or col >= COLS or board[row][col] == '.':
                return False
            board[row][col] = '.'
            dfs(row, col+1)
            dfs(row+1, col)
            return True

        count = 0
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col):
                    count += 1

        return count

    # inplace, no modify of board
    def countBattleships(self, board: list[list[str]]) -> int:
        ROWS, COLS = len(board), len(board[0])
        count = 0
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == '.':
                    continue
                if (col == 0 or board[row][col-1] == '.') and (row == 0 or board[row-1][col] == '.'):
                    count += 1
        
        return count