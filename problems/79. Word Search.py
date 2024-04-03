# link: https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = set()
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(row, col, i):
            if i == len(word):
                return True
            if row < 0 or col < 0 or row >= m or col >= n:
                return False
            if (row, col) in visited:
                return False
            if word[i] != board[row][col]:
                return False

            visited.add((row, col))
            for dx, dy in dirs:
                if dfs(row+dx, col+dy, i+1):
                    return True
            visited.remove((row, col))

            return False


        for row in range(m):
            for col in range(n):
                visited = set()
                if dfs(row, col, 0):
                    return True

        return False
