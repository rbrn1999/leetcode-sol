# link: https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        dp = [[float('inf')] * (n+1) for _ in range(2)]
        dp[0][n] = 1

        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                dp[0][col] = min(dp[1][col], dp[0][col+1]) - dungeon[row][col]
                dp[0][col] = max(dp[0][col], 1)

            dp[1] = dp[0]
            dp[0] = [float('inf')] * (n+1)

        return dp[1][0]
