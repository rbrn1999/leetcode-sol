# link: https://leetcode.com/problems/n-queens/
# solution: https://leetcode.com/problems/n-queens/discuss/19971

    def solveNQueens(self, n: int) -> List[List[str]]:
        queens = [-1]*n # index: row, value: column
        result = []

        def valid(i):
            for j in range(i):
                if abs(queens[j] - queens[i]) == i-j or queens[j] == queens[i]: # on same diagnal or same column
                    return False
            return True

        def dfs(index):
            nonlocal n
            if index == n:
                board = []
                board_2d = [['.']*n for _ in range(n)]
                for row, col in enumerate(queens):
                    board_2d[row][col] = 'Q'
                for row in board_2d:
                    board.append(''.join(row))
                result.append(board)
                return

            for i in range(len(queens)):
                queens[index] = i
                if valid(index):
                    dfs(index+1)

        dfs(0)
        return result
