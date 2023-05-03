# link: https://leetcode.com/problems/unique-binary-search-trees/

# top-bottom
from functools import cache
class Solution:
    @cache
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 1
        return sum(self.numTrees(mid) * self.numTrees(n-(mid+1)) for mid in range(n))

# bottom-up
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] + [0] * n
        for i in range(1, n+1):
            dp[i] = sum(dp[root-1] * dp[i-root] for root in range(1, i+1))    
        return dp[n]
        