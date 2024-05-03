# link: https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/

# Approach 1
class Solution:
    def removeOnes(self, grid: list[list[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        for col in range(n):
            if grid[0][col] == 1:
                continue
            for row in range(1, m):
                grid[row][col] = (grid[row][col] + 1) % 2

        for row in range(1, m):
            total = sum(grid[row])
            if total != 0 and total != n:
                return False

        return True

# Approach 2
class Solution:
    def removeOnes(self, grid: list[list[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        for row in range(1, m):
            val = grid[0][0] ^ grid[row][0]
            for col in range(1, n):
                if grid[row][col] ^ grid[0][col] != val:
                    return False

        return True
