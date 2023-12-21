# link: https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        x_points = set()
        for x, y in points:
            x_points.add(x)
        
        sorted_x = sorted(x_points)
        ans = 0
        for i in range(1, len(sorted_x)):
            ans = max(ans, sorted_x[i] - sorted_x[i-1])
        
        return ans