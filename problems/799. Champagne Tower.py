# link: https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        cur = [poured]
        for r in range(1, query_row+1):
            prev = cur
            cur = [0] * (r+1)
            for g in range(r+1):
                cur[g] = (0 if g == 0 else max(0, prev[g-1]-1)/2) + (0 if g == r else max(0, prev[g]-1)/2)

        return min(cur[query_glass], 1)