# link: https://leetcode.com/problems/strange-printer/

class Solution:
    def strangePrinter(self, s: str) -> int:
        dp = [[float('inf')] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
            if i < len(s) - 1:
                dp[i][i+1] = 1 if s[i] == s[i+1] else 2

        for d in range(2, len(s)): # right - left
            for left in range(len(s)-d):
                right = left + d
                dp[left][right] = d + 1
                for i in range(left, right):
                    dp[left][right] = min(dp[left][right], dp[left][i] + dp[i+1][right])
                if s[left] == s[right]:
                    dp[left][right] -= 1

        return dp[0][-1]
