# link: https://leetcode.com/problems/cyclically-rotating-a-grid/

from functools import cache

class Solution:
    def rotateGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        newGrid = [[0]*n for _ in range(m)]
        
        @cache
        def flattened(cycle):
            height, width = m - 2*cycle, n - 2*cycle
            flat = [(cycle+i, cycle) for i in range(height-1)] \
                        + [(cycle+(height-1), cycle+j) for j in range(width-1)] \
                        + [(cycle+(height-1)-i, cycle+(width-1)) for i in range(height-1)] \
                        + [(cycle, cycle+(width-1)-j) for j in range(width-1)]
            return flat
        
        def move(i, j):
            cycle = min(i, m-1-i, j, n-1-j)
            height, width = m - 2*cycle, n - 2*cycle
            flat = flattened(cycle)
            
            offset = k
            if i != m-cycle-1 and j == cycle:
                offset += i-cycle
            elif i == m-cycle-1 and j != n-cycle-1:
                offset += height-1 + j-cycle
            elif i != 0 and j == n-cycle-1:
                offset += height-1 + width-1 + m-cycle-1-i
            else:
                offset += 2*(height-1) + width-1 + n-cycle-1-j
            
            offset %= ((height-1+width-1)*2)
            return flat[offset]
        
        for i in range(m):
            for j in range(n):
                row, col = move(i, j)
                newGrid[row][col] = grid[i][j]
        return newGrid