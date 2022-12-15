# link: https://leetcode.com/problems/delete-greatest-value-in-each-row/

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort(reverse=True)
        m = len(grid)
        n = len(grid[0])
        result = 0
        for c in range(n):
            curMax = 0
            for r in range(m):
                curMax = max(curMax, grid[r][c])

            result += curMax

        return result
