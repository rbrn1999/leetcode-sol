# link: https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:
        queens = [-1]*n # index: row, value: column
        solutionCount = 0

        def valid(i):
            for j in range(i):
                if abs(queens[j] - queens[i]) == i-j or queens[j] == queens[i]: # on same diagnal or same column
                    return False
            return True

        def dfs(index):
            nonlocal n, solutionCount
            if index == n:
                solutionCount += 1
                return

            for i in range(len(queens)):
                queens[index] = i
                if valid(index):
                    dfs(index+1)

        dfs(0)
        return solutionCount
