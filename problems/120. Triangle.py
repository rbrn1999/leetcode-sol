# link: https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        @cache
        def dfs(row, i):
            if row < n-1:
                return triangle[row][i] + min(dfs(row+1, i), dfs(row+1, i+1))
            return triangle[row][i]

        return dfs(0, 0)
