# link: https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        for _ in range(3, n+1):
            dp = [dp[1], dp[2], sum(dp)]
        return dp[2] if n > 2 else dp[n]
