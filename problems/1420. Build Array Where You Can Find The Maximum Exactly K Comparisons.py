# link: https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/

from functools import cache
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        @cache
        def helper(i, max_num, cost):
            if cost > k:
                return 0
            if i == n:
                return int(cost == k)
            ways = 0
            if n-i >= k-cost:
                ways += max_num * helper(i+1, max_num, cost)
                ways %= (10 ** 9 + 7)
            if cost < k:
                ways += sum(helper(i+1, max_num+j, cost+1) for j in range(1, m-max_num+1))
                ways %= (10 ** 9 + 7)
            return ways
        
        return helper(0, 0, 0)