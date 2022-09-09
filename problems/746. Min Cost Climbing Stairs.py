# link: https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def minCost(index):
            if index < 2:
                return 0
            return min(cost[index-1] + minCost(index-1), cost[index-2] + minCost(index-2))

        return minCost(len(cost))
