# link: https://leetcode.com/problems/my-calendar-ii/

# Brute Force
import bisect
class MyCalendarTwo:

    def __init__(self):
        self.starts = []
        self.ends = []


    def book(self, start: int, end: int) -> bool:
        i = bisect.bisect_left(self.starts, start)
        j = bisect.bisect_left(self.ends, end)
        starts = self.starts.copy()
        ends = self.ends.copy()
        starts.insert(i, start)
        ends.insert(j, end)


        i = 0
        overlaps = 0
        for s in starts:
            while i < len(ends) and s >= ends[i]:
                i += 1
                overlaps -= 1
            overlaps += 1
            if overlaps == 3:
                return False

        self.starts = starts
        self.ends = ends
        return True


# Line Sweep
from sortedcontainers import SortedDict

class MyCalendarTwo:

    def __init__(self):
        self.booking_count = SortedDict()
        self.max_overlapped_booking = 2


    def book(self, start: int, end: int) -> bool:
        self.booking_count[start] = self.booking_count.get(start, 0) + 1
        self.booking_count[end] = self.booking_count.get(end, 0) - 1

        overlapped_booking = 0

        for count in self.booking_count.values():
            overlapped_booking += count

            if overlapped_booking > self.max_overlapped_booking:
                self.booking_count[start] -=  1
                self.booking_count[end] += 1

                if self.booking_count[start] == 0:
                    del self.booking_count[start]
                if self.booking_count[end] == 0:
                    del self.booking_count[end]

                return False

        return True

# Overlapped Intervals

class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.overlaps = []


    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlaps:
            if self.does_overlap(start, end, s, e):
                return False

        for s, e in self.bookings:
            if self.does_overlap(start, end, s, e):
                self.overlaps.append(self.get_overlapped(start, end, s, e))

        self.bookings.append((start, end))
        return True

    def does_overlap(self, start1: int, end1: int, start2: int, end2: int) -> bool:
        return max(start1, start2) < min(end1, end2)

    def get_overlapped(self, start1: int, end1: int, start2: int, end2: int) -> tuple[int, int]:
        return max(start1, start2), min(end1, end2)



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
