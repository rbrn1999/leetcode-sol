# link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

# Top-Down
from functools import cache
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        @cache
        def dfs(i: int, hold: bool, t: int) -> int:
            if t == 0:
                return 0
            if i == len(prices):
                return 0
            
            # skip
            profit = dfs(i+1, hold, t)
            # buy
            if not hold:
                profit = max(profit, -prices[i] + dfs(i+1, True, t))
            # sell
            if hold:
                profit = max(profit, prices[i] + dfs(i+1, False, t-1))
            
            return profit
        
        return dfs(0, False, 2)
    
# Bottom-Up
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        t1_hold, t2_hold = -float('inf'), -float('inf') # profit of holding
        t1_sold, t2_sold = 0, 0 # profit of selling (not holding stocks)

        for price in prices:
            t1_hold = max(t1_hold, -price)
            t1_sold = max(t1_sold, t1_hold + price)

            t2_hold = max(t2_hold, t1_sold - price)
            t2_sold = max(t2_sold, t2_hold + price)
        
        return t2_sold