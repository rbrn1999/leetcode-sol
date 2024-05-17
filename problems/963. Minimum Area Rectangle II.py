# link: https://leetcode.com/problems/minimum-area-rectangle-ii/

import itertools
import math
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        result = float('inf')
        n = len(points)
        points_set = set(tuple(point) for point in points)
        for i, j, k in itertools.combinations(range(n), 3):
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]
            if (x1-x2) * (x1-x3) + (y1-y2) * (y1-y3) == 0:
                x4, y4 = x3 - (x1-x2), y3 - (y1-y2)
                if (x4, y4) in points_set:
                    area = math.sqrt((x1-x2)**2 + (y1-y2)**2) * math.sqrt((x1-x3)**2 + (y1-y3)**2)
                    result = min(result, area)
            if (x2-x1) * (x2-x3) + (y2-y1) * (y2-y3) == 0:
                x4, y4 = x3 - (x2-x1), y3 - (y2-y1)
                if (x4, y4) in points_set:
                    area = math.sqrt((x2-x1)**2 + (y2-y1)**2) * math.sqrt((x2-x3)**2 + (y2-y3)**2)
                    result = min(result, area)
            if (x3-x1) * (x3-x2) + (y3-y1) * (y3-y2) == 0:
                x4, y4 = x2 - (x3-x1), y2 - (y3-y1)
                if (x4, y4) in points_set:
                    area = math.sqrt((x3-x1)**2 + (y3-y1)**2) * math.sqrt((x3-x2)**2 + (y3-y2)**2)
                    result = min(result, area)


        return result if result < float('inf') else 0.0
