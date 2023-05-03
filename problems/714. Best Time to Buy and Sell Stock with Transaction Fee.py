# link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold, not_holding = float('-inf'), 0
        for price in prices:
            hold, not_holding = max(hold, not_holding-price), max(not_holding, hold+price-fee)
        return not_holding
