# link: https://leetcode.com/problems/out-of-boundary-paths/

from functools import cache

# DP
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = 0
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1

        for _ in range(maxMove):
            next_dp = [[0] * n for _ in range(m)]
            for row in range(m):
                for col in range(n):
                    for x, y in dirs:
                        nr, nc = row + x, col + y
                        if nr < 0 or nc < 0 or nr == m or nc == n:
                            result = (result + dp[row][col]) % (10 ** 9 + 7)
                        else:
                            next_dp[nr][nc] = (next_dp[nr][nc] + dp[row][col]) % (10 ** 9 + 7)

            dp = next_dp
        
        return result

# Recursion + Memoization
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        @cache
        def dfs(row: int, col: int, moves: int) -> int:
            if row < 0 or col < 0 or row >= m or col >= n:
                return 1
            if moves == 0:
                return 0
            count = 0
            for x, y in dirs:
                count = (count +  dfs(row + x, col + y, moves-1)) % (10 ** 9 + 7)
            
            return count
        
        return dfs(startRow, startColumn, maxMove)
