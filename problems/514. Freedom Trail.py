# link: https://leetcode.com/problems/freedom-trail/

# Bottom-Up DP
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        m, n = len(ring), len(key)
        dp = [float('inf')] * m
        for i in range(len(ring)):
            if ring[i] == key[0]:
                dp[i] = 1 + min(i, m-i)

        for i in range(1, len(key)):
            new_dp = [float('inf')] * m
            for j in range(len(ring)):
                if dp[j] == float('inf'):
                    continue
                for k in range(len(ring)):
                    if ring[k] != key[i]:
                        continue
                    new_dp[k] = min(new_dp[k], 1 + dp[j] + min((k - j + m) % m, (j - k + m) % m))
            dp = new_dp

        result = min(dp)
        return result if type(result) is int else -1
