# link: https://leetcode.com/problems/rectangle-area/

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        rect1 = (ax2 - ax1) * (ay2 - ay1)
        rect2 = (bx2 - bx1) * (by2 - by1)
        overlap = max(0, (min(ax2, bx2) - max(ax1, bx1))) * max(0, (min(ay2, by2) - max(ay1, by1)))
        return rect1 + rect2 - overlap
