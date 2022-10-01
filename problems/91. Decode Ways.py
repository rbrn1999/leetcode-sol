# link: https://leetcode.com/problems/decode-ways/
# solution reference: https://leetcode.com/problems/decode-ways/discuss/30358/

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = len(s) * [0]
        dp[0] = 1 if s[0] != '0' else 0
        for i in range(1, len(s)):
            if s[i] != '0':
                dp[i] += dp[i-1]
            if 10 <= int(s[i-1:i+1]) <= 26:
                if i < 2:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-2]

        return dp[-1]

