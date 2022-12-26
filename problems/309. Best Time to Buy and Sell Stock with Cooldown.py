# link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dfs(i, hold):
            if i >= n:
                return 0
            if hold:
                sell_profit = prices[i] + dfs(i+2, False)
                hold_profit = dfs(i+1, True)
                return max(sell_profit, hold_profit)
            else:
                buy_profit = -prices[i] + dfs(i+1, True)
                hold_profit = dfs(i+1, False)
                return max(buy_profit, hold_profit)

        return dfs(0, False)

