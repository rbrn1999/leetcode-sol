# link: https://leetcode.com/problems/unique-paths-ii/

from functools import lru_cache
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        @lru_cache(maxsize=None)
        def dfs(i, j): # return number of paths from [i][j] to [M-1][N-1]
            if i == M-1 and j == N-1: # base case
                return 1
            right = dfs(i+1, j) if i<M-1 and obstacleGrid[i+1][j] == 0 else 0
            down  = dfs(i, j+1) if j<N-1 and obstacleGrid[i][j+1] == 0 else 0
            return right + down
            
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        else:        
            return dfs(0,0)