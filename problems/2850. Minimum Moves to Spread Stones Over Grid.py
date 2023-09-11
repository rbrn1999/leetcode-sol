# link: https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/

class Solution:
    def minimumMoves(self, grid: list[list[int]]) -> int:
        extras = {}
        zeros = []
        for row in range(3):
            for col in range(3):
                if grid[row][col] > 1:
                    extras[(row, col)] = grid[row][col] - 1
                elif grid[row][col] == 0:
                    zeros.append((row, col))
        def dfs(i):
            if i == len(zeros):
                return 0
            row, col = zeros[i]
            cost = float('inf')
            for r, c in extras:
                if extras[(r, c)] == 0:
                    continue
                extras[(r, c)] -= 1
                cost = min(cost, abs(row-r) + abs(col-c) + dfs(i+1))
                extras[(r, c)] += 1

            return cost
        
        return dfs(0) 
            