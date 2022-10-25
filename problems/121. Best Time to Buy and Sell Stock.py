# link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        high = -float('inf')
        profit = 0
        
        for price in prices:
            if price < low:
                low = high = price
            elif price > high:
                high = price
                profit = max(profit, high-low)
                
        return profit