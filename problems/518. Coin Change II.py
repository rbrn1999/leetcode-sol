class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        combinations = 0
        memo = {}
        def helper(accu, i):
            if (accu, i) in memo:
                pass
            elif accu == amount:
                memo[(accu, i)] = 1
            elif i >= n:
                 memo[(accu, i)] = 0
            else:
                memo[(accu, i)] = 0
                for coin_count in range((amount - accu) // coins[i] + 1):
                    if coin_count * coins[i] + accu > amount:
                        break
                    memo[(accu, i)] += helper(accu + coins[i] * coin_count, i+1)
            return memo[(accu, i)]

        return helper(0, 0)