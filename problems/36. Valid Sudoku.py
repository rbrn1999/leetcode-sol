# link: https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        for i in range(n):
            s = set()
            for j in range(n):
                if board[i][j] == '.':
                    continue
                if board[i][j] in s:
                    return False
                else:
                    s.add(board[i][j])

        for i in range(n):
            s = set()
            for j in range(n):
                if board[j][i] == '.':
                    continue
                if board[j][i] in s:
                    return False
                else:
                    s.add(board[j][i])


        for i in range(3):
            for j in range(3):
                s = set()
                for r in range(3*i, 3*i+3):
                    for c in range(3*j, 3*j+3):
                        if board[r][c] == '.':
                            continue
                        if board[r][c] in s:
                            return False
                        else:
                            s.add(board[r][c])

        return True

