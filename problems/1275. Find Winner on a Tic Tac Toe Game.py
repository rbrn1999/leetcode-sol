# link: https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [['_'] * 3 for _ in range(3)]
        for i in range(len(moves)):
            row, col = moves[i]
            grid[row][col] = 'A' if i%2 == 0 else 'B'

        for row in grid:
            if row[0] == '_':
                continue
            if row[0] == row[1] and row[0] == row[2]:
                return row[0]

        for col in range(3):
            if grid[0][col] == '_':
                continue
            if grid[0][col] == grid[1][col] and grid[0][col] == grid[2][col]:
                return grid[0][col]

        if grid[0][0] != '_' and grid[0][0] == grid[1][1] and grid[0][0] == grid[2][2]:
            return grid[0][0]
        if grid[2][0] != '_' and grid[2][0] == grid[1][1] and grid[2][0] == grid[0][2]:
            return grid[2][0]

        return "Draw" if len(moves) == 9 else "Pending"


