# link: https://leetcode.com/problems/count-ways-to-build-good-strings/

from functools import cache
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        @cache
        def dfs(length):
            if length == 0:
                return 1
            if length < 0:
                return 0
            return (dfs(length-one) + dfs(length-zero)) % int(1E9 + 7)

        return sum([dfs(i) for i in range(low, high+1)]) % int(1E9 + 7)
