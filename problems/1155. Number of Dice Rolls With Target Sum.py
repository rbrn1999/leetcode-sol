# link: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
# You have n dice and each die has k faces numbered from 1 to k.

# Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.

 

# Example 1:

# Input: n = 1, k = 6, target = 3
# Output: 1
# Explanation: You throw one die with 6 faces.
# There is only one way to get a sum of 3.
# Example 2:

# Input: n = 2, k = 6, target = 7
# Output: 6
# Explanation: You throw two dice, each with 6 faces.
# There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
# Example 3:

# Input: n = 30, k = 30, target = 500
# Output: 222616187
# Explanation: The answer must be returned modulo 109 + 7.
 

# Constraints:

# 1 <= n, k <= 30
# 1 <= target <= 1000

from functools import lru_cache

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @lru_cache(None) # same as @cache in Python >= 3.9
        def dfs(n, target) -> int:
            # the path(permutation) will be valid if and only if the sum of n dice rolls equals to target (return 1)
            # otherwise, it's invalid (return 0)
            if n == 0:
                return 1 if target == 0 else 0
            if target < 0:
                return 0

            # sum all possible dice rolls (1~k) for round n 
            # (backtracking) =>
            # sum all possible dice rolls (1~k) for round n-1
            # ...
            # sum all possible dice rolls (1~k) for round 1 
            # (target should be in range of (1~k) to be valid. Otherwise, we can't solve it in 1 round) =>
            # sum all possible dice rolls (1~k) for round 0
            return sum(dfs(n-1, target-i) for i in range(1, k+1))
        
        return dfs(n, target) % int(1e9 + 7)