# link: https://leetcode.com/problems/out-of-boundary-paths/

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        count = 0
        dp = [[0]*n for _ in range(m)]
        dp[startRow][startColumn] = 1

        for _ in range(maxMove):
            temp = [[0]*n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == m-1:
                        count += dp[i][j]
                    if j == n-1:
                        count += dp[i][j]
                    if i == 0:
                        count += dp[i][j]
                    if j == 0:
                        count += dp[i][j]

                    # count %= int(1E9+7) # may prevent possible overflow in other language

                    temp[i][j] = ((dp[i-1][j] if i>0 else 0) + (dp[i+1][j] if i<m-1 else 0) + (dp[i][j-1] if j>0 else 0) + (dp[i][j+1] if j<n-1 else 0)) # % int(1E9 + 7)

            dp = temp

        return count % int(1E9 + 7)

