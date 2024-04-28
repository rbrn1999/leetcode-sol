# link: https://leetcode.com/problems/distinct-subsequences/

# Top-Down
from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        @cache
        def dfs(i: int, j: int):
            if j == n:
                return 1
            if i == m:
                return 0

            count = 0
            if s[i] == t[j]:
                count += dfs(i+1, j+1)
            count += dfs(i+1, j)
            return count

        return dfs(0, 0)

# Bottom-Up
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[1] * (1+m), [0] * (1+m)]

        for j in range(n):
            for i in range(m):
                dp[1][i+1] += dp[1][i]
                if s[i] == t[j]:
                    dp[1][i+1] += dp[0][i]
            dp = [dp[1], [0] * (m+1)]

        return dp[0][m]
