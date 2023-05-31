from functools import cache
class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        @cache
        def helper(i): # return: diff (a-b)
            if i == n:
                return 0
            diff = -float('inf')
            preSum = 0
            for j in range(min(3, n-i)):
                preSum += stoneValue[i+j]
                diff = max(diff, preSum - helper(i+j+1)) # negative -> change of player
            return diff

        diff = helper(0)
        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"