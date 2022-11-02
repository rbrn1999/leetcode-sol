class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        def drop(i, j):
            if (grid[i+1][j] == 1 and (j >= n-1 or grid[i+1][j+1] == -1)):
                return 0
            if (grid[i+1][j] == -1 and (j <= 0 or grid[i+1][j-1] == 1)): 
                return 0
            else:
                return grid[i+1][j]
        
        res = [-1]*n
        for col in range(n):
            ind = col
            row = -1
            flag = True
            for row in range(-1, m-1):
                stat = drop(row, col)
                if stat == 0:
                    flag = False
                    break
                else:
                    col += stat
            if flag:
                res[ind] = col
        
        return res
                    