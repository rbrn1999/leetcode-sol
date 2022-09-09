# link: https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        minCoins = [float('inf')] * (amount + 1)
        minCoins[0] = 0
        for coin in coins:
            for target in range(1, len(minCoins)):
                if coin <= target:
                    minCoins[target] = min(minCoins[target], minCoins[target-coin] + 1)
        return minCoins[amount] if minCoins[amount] != float('inf') else -1