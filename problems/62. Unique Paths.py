# link: https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0] * n for _ in range(m)]
        paths[0][0] = 1
        def findPathCount(row, col):
            if paths[row][col] != 0:
                return paths[row][col]
            if row < 0 or col < 0 or row >= m or col >= n:
                return 0
            count = findPathCount(row-1, col) + findPathCount(row, col-1)
            paths[row][col] = count
            return count
        
        return findPathCount(m-1, n-1)

# bottom-up
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            m, n = n, m
        dp = [[1]*n, [0]*n]

        for _ in range(m-1):
            for col in range(n):
                dp[1][col] = dp[0][col] + (dp[1][col-1] if col > 0 else 0)
            dp[0] = dp[1]
            dp[1] = [0] * n
        
        return dp[0][n-1]

# combinations
from functools import reduce
import operator
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            m, n = n, m
        if n == 1:
            return 1
        return reduce(operator.mul, range(m, m+n-1)) // reduce(operator.mul, range(1, n))