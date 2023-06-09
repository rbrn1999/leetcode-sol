# link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        if m < n:
            for row in range(m):
                low = 0
                high = n
                while low < high:
                    mid = low + (high - low) // 2
                    if grid[row][mid] < 0:
                        high = mid
                    else:
                        low = mid + 1
                count += n - low
        else:
            for col in range(n):
                low = 0
                high = m
                while low < high:
                    mid = low + (high - low) // 2
                    if grid[mid][col] < 0:
                        high = mid
                    else:
                        low = mid + 1
                count += m - low

        return count

