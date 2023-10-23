# link: https://leetcode.com/problems/construct-product-matrix/

class Solution:
    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        prev = 1
        ans = [[0] * n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                ans[row][col] = prev
                prev *= grid[row][col] % 12345
                prev %= 12345
        
        prev = 1
        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                ans[row][col] *= prev
                ans[row][col] %= 12345
                prev *= grid[row][col] % 12345
                prev %= 12345
        
        return ans