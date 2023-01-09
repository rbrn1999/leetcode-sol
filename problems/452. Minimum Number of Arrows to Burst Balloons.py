# link: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        points.append([float('inf'), float('inf')])
        prev_end = points[0][1]
        arrow_count = 0
        for start, end in points:
            if start > prev_end:
                prev_end = end
                arrow_count += 1
            else:
                prev_end = min(prev_end, end)

        return arrow_count

