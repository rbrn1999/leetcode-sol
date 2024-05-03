# link: https://leetcode.com/problems/my-calendar-i/

from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.intervals = SortedList()

    def book(self, start: int, end: int) -> bool:
        index = self.intervals.bisect_left((start, end))
        if index > 0 and self.intervals[index-1][1] > start:
            return False
        if index < len(self.intervals) and self.intervals[index][0] < end:
            return False

        self.intervals.add((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
