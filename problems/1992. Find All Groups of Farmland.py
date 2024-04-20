# link: https://leetcode.com/problems/find-all-groups-of-farmland/

import itertools
class Solution:
    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        m, n = len(land), len(land[0])

        def helper(r, c) -> list[int]:
            while r < m and land[r][c] == 1:
                r += 1
            while c < n and land[r-1][c] == 1:
                c += 1

            return [r-1, c-1]

        result = []

        for r, c in itertools.product(range(m), range(n)):
            if land[r][c] == 1 and (r == 0 or land[r-1][c] == 0) and (c == 0 or land[r][c-1] == 0):
                r2, c2 = helper(r, c)
                result.append([r, c, r2, c2])

        return result
