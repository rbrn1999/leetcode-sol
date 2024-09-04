# link: https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) != m * n:
            return []

        result = [[0] * n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                result[row][col] = original[row * n + col]

        return result
