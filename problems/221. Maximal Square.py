# link: https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n+1) for _ in range(m+1)]

        answer = 0
        for row in range(1, m+1):
            for col in range(1, n+1):
                if matrix[row-1][col-1] == '0':
                    continue
                dp[row][col] = min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1]) + 1
                answer = max(answer, dp[row][col] * dp[row][col])

        return answer

