# link: https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0] * n for _ in range(m)]
        paths[0][0] = 1
        def findPathCount(row, col):
            if paths[row][col] != 0:
                return paths[row][col]
            if row < 0 or col < 0 or row >= m or col >= n:
                return 0
            count = findPathCount(row-1, col) + findPathCount(row, col-1)
            paths[row][col] = count
            return count
        
        return findPathCount(m-1, n-1)