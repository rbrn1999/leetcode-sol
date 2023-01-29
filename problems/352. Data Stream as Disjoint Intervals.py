# link: https://leetcode.com/problems/data-stream-as-disjoint-intervals/

from sortedcontainers import SortedDict
class SummaryRanges:

    def __init__(self):
        self.intervals = SortedDict() # key: start, value: end (inclusive)

    def addNum(self, value: int) -> None:
        index = self.intervals.bisect_left(value)
        starts = self.intervals.iloc
        if len(self.intervals) > index and starts[index]-value == 1 and value-self.intervals[starts[index-1]] == 1:
            self.intervals[starts[index-1]] = self.intervals[starts[index]]
            self.intervals.pop(starts[index])
        elif index > 0 and self.intervals[starts[index-1]] + 1 == value:
            self.intervals[starts[index-1]] += 1
        elif index < len(self.intervals) and starts[index] - 1 == value:
            end = self.intervals[starts[index]]
            self.intervals.pop(starts[index])
            self.intervals[value] = end
        elif (index < len(self.intervals) and value == starts[index]) or (index > 0 and self.intervals[starts[index-1]] >= value):
            pass
        else:
            self.intervals[value] = value

    def getIntervals(self) -> List[List[int]]:
        return [list(item) for item in self.intervals.items()]


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
