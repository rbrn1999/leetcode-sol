# link: https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/

class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [0] + [float('inf')] * n
        for r in range(n):
            for l in range(r+1):
                if s[l] == '0':
                    continue
                num = int(s[l:r+1], 2)
                while num > 0 and num % 5 == 0:
                    num //= 5
                if num == 1:
                    dp[r+1] = min(dp[r+1], dp[l] + 1)

        return dp[n] if dp[n] != float('inf') else -1
