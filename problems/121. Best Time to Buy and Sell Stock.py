# link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low = float('inf')
        profit = 0
        for price in prices:
            if price > low:
                profit = max(profit, price-low)
            else:
                low = price
        
        return profit