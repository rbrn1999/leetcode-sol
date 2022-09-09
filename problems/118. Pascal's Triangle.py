# link: https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = [[1]]
        for row in range(1, numRows):
            triangle.append([1] + [0]*(row-1) + [1])
            for i in range(1, ceil((row+1) / 2)):
                triangle[row][i] = triangle[row][-(i+1)] = triangle[row-1][i-1] + triangle[row-1][i]
        return triangle
