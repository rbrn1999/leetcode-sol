# link: https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        if arrLen == 1:
            return 1
        n = min(arrLen, 1 + steps // 2)
        dp = [1] + [0] * (n-1)
        for _ in range(steps):
            temp = [0] * n
            temp[0] = (dp[0] + dp[1]) % (10 ** 9 + 7)
            temp[-1] = (dp[-2] + dp[-1]) % (10 ** 9 + 7)
            for i in range(1, n-1):
                temp[i] = (temp[i-1] - (dp[i-2] if i > 1 else 0) + dp[i+1]) % (10 ** 9 + 7)
            dp = temp

        return dp[0]