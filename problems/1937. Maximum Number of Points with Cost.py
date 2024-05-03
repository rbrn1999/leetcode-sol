# link: https://leetcode.com/problems/maximum-number-of-points-with-cost/

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        m, n = len(points), len(points[0])
        maxVals = points[0].copy()

        for row in range(1, m):
            left_maxs = [0] * n # [0, i)
            right_maxs = [0] * (n-1) + [maxVals[-1]] # [i, n-1]

            for col in range(1, n):
                left_maxs[col] = max(left_maxs[col-1]-1, maxVals[col-1]-1)

            for col in range(n-2, -1, -1):
                right_maxs[col] = max(right_maxs[col+1]-1, maxVals[col])

            for col in range(n):
                maxVals[col] = points[row][col] + max(left_maxs[col], right_maxs[col])

        return max(maxVals)
