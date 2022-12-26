# link: https://leetcode.com/problems/domino-and-tromino-tiling/

from functools import cache
class Solution:
    def numTilings(self, n: int) -> int:
        prevState = 2 # 0: two slots, 1: 1 slot, 2: no slots
        @cache
        def dfs(col, prevState):
            if col == n-1:
                return 1
            col += 1
            if prevState == 0:
                return dfs(col, 2) + 2 * dfs(col, 1) % int(1E9 + 7)
            elif prevState == 1:
                return dfs(col, 2) + dfs(col, 1) % int(1E9 + 7)
            else:
                return dfs(col, 2) + dfs(col, 0) % int(1E9 + 7)

        return dfs(0, prevState) % int(1E9 + 7)
