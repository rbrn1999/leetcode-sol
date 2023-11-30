# link: https://leetcode.com/problems/largest-submatrix-with-rearrangements/

# Sort by consecutive ones for each row
class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ones = [0] * n
        ans = 0
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 1:
                    ones[col] += 1
                else:
                    ones[col] = 0

            height = m
            for i, num in enumerate(sorted(ones, reverse=True)):
                if num == 0:
                    break
                height = min(num, height)
                ans = max(ans, height * (i+1))
        
        return ans