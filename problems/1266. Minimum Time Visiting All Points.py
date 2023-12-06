# link: https://leetcode.com/problems/minimum-time-visiting-all-points/
class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        distance = 0
        for i in range(1, len(points)):
            distance += max(abs(points[i][0]-points[i-1][0]), abs(points[i][1]-points[i-1][1]))
        return distance