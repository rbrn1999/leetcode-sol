# link: https://leetcode.com/problems/count-sub-islands/

import itertools
class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        visited = set()
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ROW, COL = len(grid1), len(grid1[0])
        def dfs(row: int, col: int) -> bool:
            if (
                row < 0 or row >= ROW or col < 0 or col >= COL
                or (row, col) in visited
                or grid2[row][col] == 0
            ):
                return True

            visited.add((row, col))
            isValid = True

            if grid1[row][col] == 0:
                isValid = False
            
            for dr, dc in dirs:
                nr, nc = row+dr, col+dc
                if not dfs(nr, nc):
                    isValid = False
            
            return isValid
            
        
        subIslands = 0
        for row, col in itertools.product(range(ROW), range(COL)):
            if (
                (row, col) not in visited and grid2[row][col] == 1
                and dfs(row, col)
            ):
                subIslands += 1
        
        return subIslands