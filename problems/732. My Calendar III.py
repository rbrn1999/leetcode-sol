# link: https://leetcode.com/problems/my-calendar-iii/
# solution reference: https://leetcode.com/problems/my-calendar-iii/solution/

# Sweep line algorithm
from sortedcontainers import SortedDict
class MyCalendarThree:

    def __init__(self):
        self.diff = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.diff[start] = self.diff.get(start, 0) + 1
        self.diff[end] = self.diff.get(end, 0) - 1

        cur = max_count = 0
        # to cummulate the count, the order matters here => use SortedDict
        for key in self.diff:
            cur += self.diff[key]
            max_count = max(max_count, cur)

        return max_count

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
