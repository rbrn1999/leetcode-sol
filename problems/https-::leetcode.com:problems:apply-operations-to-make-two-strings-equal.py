# link: https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/

class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        diffs = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffs.append(i)
        
        if len(diffs) % 2 == 1:
            return -1
        
        dp = {-1: 0, 0: x/2}

        def dfs(i: int) -> float:
            if i in dp:
                return dp[i]
            dp[i] = min(diffs[i]-diffs[i-1]+dfs(i-2), x/2 + dfs(i-1))
            return dp[i]

        return int(dfs(len(diffs)-1))