# link: https://leetcode.com/problems/number-of-islands/

from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def search(x, y):
            if x<0 or x>=m or y<0 or y>=n:
                return
            if grid[x][y] == '1':
                grid[x][y] = '0'
                search(x-1, y)
                search(x+1, y)
                search(x, y-1)
                search(x, y+1)
                
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    search(i, j)
        
        return count

output = Solution().numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])

print(output)