# link: https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        memo = {}
        def helper(start, end, i, j):
            key = (start, end)
            if i > j:
                return 0
            if key in memo:
                return memo[key]
            
            memo[key] = end-start + min(helper(start, cuts[ind], i, ind-1) + helper(cuts[ind], end, ind+1, j) for ind in range(i, j+1))
            return memo[key]

            
        cuts.sort()
        return helper(0, n, 0, len(cuts)-1)
