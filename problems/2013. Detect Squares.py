# link: https://leetcode.com/problems/detect-squares/

import collections
class DetectSquares:

    def __init__(self):
        self.pointCounts = {}
        self.x = collections.defaultdict(set)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.pointCounts[(x, y)] = self.pointCounts.get((x, y), 0) + 1
        self.x[x].add(y)

    def count(self, point: List[int]) -> int:
        count = 0
        x1, y1 = point
        for y2 in self.x[x1]:
            if y1 == y2:
                continue
            side = abs(y2 - y1)
            if (x1 + side, y1) in self.pointCounts and (x1 + side, y2) in self.pointCounts:
                count += self.pointCounts[(x1 + side, y1)] * self.pointCounts[(x1 + side, y2)] * self.pointCounts[(x1, y2)]
            if (x1 - side, y1) in self.pointCounts and (x1 - side, y2) in self.pointCounts:
                count += self.pointCounts[(x1 - side, y1)] * self.pointCounts[(x1 - side, y2)] * self.pointCounts[(x1, y2)]
        return count


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
