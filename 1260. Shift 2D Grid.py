# link: https://leetcode.com/problems/shift-2d-grid/

from typing import List
class Solution:
    # time: O(m*n), space: O(1)
    # treat 2D grid as 1D array
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k %= m*n
        def reverse(low, high):
            while low < high:
                grid[low // n][low % n], grid[high // n][high % n] = grid[high // n][high % n],  grid[low // n][low % n]
                low += 1
                high -= 1

        reverse(0, m*n - 1) # move last k elements to the start of the grid
        reverse(0, k - 1) # restore the order of the first k elements
        reverse(k, m*n - 1) # restore the rest of the grid
            
        return grid
            

grid = [[0,1,2,3],[4,5,6,7],[8,9,10,12],[12,13,14,15]]
k = 4

print(Solution().shiftGrid(grid, k))