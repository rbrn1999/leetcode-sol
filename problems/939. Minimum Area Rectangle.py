# link: https://leetcode.com/problems/minimum-area-rectangle/description

class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        min_area = float('inf')
        points_set = set(tuple(point) for point in points)

        n = len(points)
        for i in range(n-1):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2:
                    continue
                if (x1, y2) in points_set and (x2, y1) in points_set:
                    area = abs(x2-x1) * abs(y2-y1)
                    min_area = min(min_area, area)

        return min_area if type(min_area) != float('inf') else 0
