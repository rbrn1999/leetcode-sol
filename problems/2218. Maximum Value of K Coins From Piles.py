# link: https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

from functools import cache
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        prefixSums = []
        for pile in piles:
            prefixSums.append([pile[0]])
            for i in range(1, len(pile)):
                prefixSums[-1].append(pile[i] + prefixSums[-1][i-1])

        @cache
        def helper(pile_ind, coins) -> int:
            if coins == 0:
                return 0
            if pile_ind == len(piles) - 1:
                return prefixSums[pile_ind][min(coins-1, len(prefixSums[pile_ind])-1)]

            return max((prefixSums[pile_ind][i] if i >= 0 else 0) + helper(pile_ind+1, coins-(i+1)) for i in range(-1, min(len(prefixSums[pile_ind]), coins)))

        return helper(0, k)

