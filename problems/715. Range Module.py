# link: https://leetcode.com/problems/range-module/

from sortedcontainers import SortedList

class RangeModule:

    def __init__(self):
        self.ranges = SortedList()

    def addRange(self, left: int, right: int) -> None:
        index = self.ranges.bisect_left([left, right])

        while index < len(self.ranges) and self.ranges[index][0] <= right:
            right = max(right, self.ranges[index][1])
            self.ranges.pop(index)

        index -= 1
        while index >= 0 and self.ranges[index][1] >= left:
            left = min(left, self.ranges[index][0])
            # edge case: The first range on left could cover the whole new interval: old_l--l--r--old_r
            right = max(right, self.ranges[index][1])
            self.ranges.pop(index)
            index -= 1

        self.ranges.add([left, right])

    def queryRange(self, left: int, right: int) -> bool:
        if not self.ranges:
            return False

        index = self.ranges.bisect_left([left, right])
        if index == 0:
            return self.ranges[index][0] == left
        if index == len(self.ranges):
            return self.ranges[index-1][1] >= right

        return self.ranges[index-1][1] >= right or self.ranges[index][0] == left


    def removeRange(self, left: int, right: int) -> None:
        index = self.ranges.bisect_left([left, right])

        if index > 0:
            if left < self.ranges[index-1][1]:
                prev_left, prev_right = self.ranges[index-1]
                self.ranges[index-1][1] = left
                if right < prev_right:
                    self.ranges.add([right, prev_right])
                    return

        while index < len(self.ranges) and right >= self.ranges[index][1]:
            self.ranges.pop(index)

        if index < len(self.ranges):
            self.ranges[index][0] = max(self.ranges[index][0], right)


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
