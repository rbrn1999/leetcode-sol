# link: https://leetcode.com/problems/coin-change/

# class Solution:
#     def coinChange(self, coins: list[int], amount: int) -> int:
#         minCoins = [float('inf')] * (amount+1)
#         minCoins[0] = 0 # base case: 0 coins to get to 0 total
#         for i in range(1, amount+1):
#             for coin in coins:
#                 if coin <= amount:
#                     minCoins[i] = min(minCoins[i], minCoins[i-coin]+1)
#         return minCoins[amount] if minCoins[amount] != float('inf') else -1
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        minCoins = [float('inf')] * (amount + 1)
        minCoins[0] = 0
        for coin in coins:
            for target in range(1, len(minCoins)):
                if coin <= target:
                    minCoins[target] = min(minCoins[target], minCoins[target-coin] + 1)
        return minCoins[amount] if minCoins[amount] != float('inf') else -1