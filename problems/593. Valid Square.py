# link: https://leetcode.com/problems/valid-square/

import math
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(a, b):
            x1, y1 = a
            x2, y2 = b
            return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        def valid(o, ps):
            d = [distance(o, ps[0]), distance(o, ps[1]), distance(o, ps[2])]
            if min(d) == 0:
                return False
            maxInd = d.index(max(d))
            return math.isclose(d[maxInd - 1], d[maxInd - 2]) and math.isclose(d[maxInd - 1] * sqrt(2), d[maxInd])

        points = (p1, p2, p3, p4)
        return all(valid(points[i], points[:i] + points[i+1:]) for i in range(4))


