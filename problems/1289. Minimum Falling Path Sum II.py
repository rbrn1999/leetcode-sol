# link: https://leetcode.com/problems/minimum-falling-path-sum-ii/

class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        min1, min2 = (0, -1), (0, -1) # value, index
        for row in grid:
            newMin1, newMin2 = (float('inf'), -1), (float('inf'), -1)
            for i, cell in enumerate(row):
                cost = float('inf')
                if i != min1[1]:
                    cost = min1[0] + cell
                else:
                    cost = min2[0] + cell

                if cost < newMin1[0]:
                    newMin2 = newMin1
                    newMin1 = (cost, i)
                elif cost < newMin2[0]:
                    newMin2 = (cost, i)

            min1, min2 = newMin1, newMin2

        return min(min1[0], min2[0]) if type(min1[0]) is int and type(min2[0]) is int else -1
