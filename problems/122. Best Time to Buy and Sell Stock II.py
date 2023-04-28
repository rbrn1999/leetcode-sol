# link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minPrice = float('inf')
        for price in prices:
            if price > minPrice:
                profit += price - minPrice
            minPrice = price
        
        return profit
        