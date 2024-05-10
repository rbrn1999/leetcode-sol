# link: https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/

import itertools

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        # check horizontal part
        for row in range(m):
            i = 0
            for col in range(n):
                if board[row][col] == '#' or (board[row][col] != ' ' and board[row][col] != word[i]):
                    i = 0
                    continue
                if col > 0 and i == 0 and board[row][col-1] != '#':
                    continue

                i += 1
                if i == len(word):
                    if col == n-1 or board[row][col+1] == '#':
                        return True
                    else:
                        i = 0


        for row in range(m):
            i = 0
            for col in range(n-1, -1, -1):
                if board[row][col] == '#' or (board[row][col] != ' ' and board[row][col] != word[i]):
                    i = 0
                    continue
                if col < n-1 and i == 0 and board[row][col+1] != '#':
                    continue

                i += 1
                if i == len(word):
                    if col == 0 or board[row][col-1] == '#':
                        return True
                    else:
                        i = 0

        # check vertical part
        for col in range(n):
            i = 0
            for row in range(m):
                if board[row][col] == '#' or (board[row][col] != ' ' and board[row][col] != word[i]):
                    i = 0
                    continue
                if row > 0 and i == 0 and board[row-1][col] != '#':
                    continue

                i += 1
                if i == len(word):
                    if (row == m-1 or board[row+1][col] == '#'):
                        return True
                    else:
                        i = 0

        for col in range(n):
            i = 0
            for row in range(m-1, -1, -1):
                if board[row][col] == '#' or (board[row][col] != ' ' and board[row][col] != word[i]):
                    i = 0
                    continue
                if row < m-1 and i == 0 and board[row+1][col] != '#':
                    continue

                i += 1
                if i == len(word):
                    if (row == 0 or board[row-1][col] == '#'):
                        return True
                    else:
                        i = 0

        return False
