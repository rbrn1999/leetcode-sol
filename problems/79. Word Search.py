# link: https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        # won't pass LeetCode submission OJ without checking char count first ¯\_(ツ)_/¯
        boardCount = {}
        wordCount = {}
        for i in range(m):
            for j in range(n):
                boardCount[board[i][j]] = boardCount.get(board[i][j], 0) + 1

        for c in word:
            wordCount[c] = wordCount.get(c, 0) + 1

        for c in wordCount:
            if wordCount.get(c, 0)> boardCount.get(c, 0):
                return False


        def search(row, col, i):
            if row < 0 or col < 0 or row >= m or col >= n or board[row][col] == '_' or word[i] != board[row][col]:
                return False

            if i == len(word)-1:
                return True

            tmp, board[row][col] = board[row][col], '_'

            i += 1
            found = search(row-1, col, i) or search(row+1, col, i) or search(row, col-1, i) or search(row, col+1, i)

            board[row][col] = tmp

            return found

        for row in range(m):
            for col in range(n):
                if search(row, col, 0):
                    return True
        return False

