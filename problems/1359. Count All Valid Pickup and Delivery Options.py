# link: https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options

# DP
from functools import cache
class Solution:
    def countOrders(self, n: int) -> int:
        '''
        p: remaining pickups
        d: deliveries (already picked up)
        '''
        @cache
        def dfs(p, d):
            if p == 0 and d == 0:
                return 1
            count = 0
            if p > 0:
                count += p * dfs(p-1, d+1)
            if d > 0:
                count += d * dfs(p, d-1)
            
            return count % int(10 ** 9 + 7)
        
        return dfs(n, 0)

# Math
class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
        # n! * (1 * 3 * 5 * ... * (2*n-1))
        for i in range(1, n+1):
            res *= i * (2 * i - 1)
            res %= 10 ** 9 + 7
        return res