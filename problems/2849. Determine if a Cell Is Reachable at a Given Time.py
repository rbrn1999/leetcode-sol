# link: https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy and t == 1:
            return False
        dx, dy = abs(fx - sx), abs(fy - sy)
        d = min(dx, dy) + abs(dx - dy)
        return d <= t
