# link: https://leetcode.com/problems/design-hit-counter/

# binary search

class HitCounter:

    def __init__(self):
        self.time_hits = [[0, 0]] # [timestamp, totalhits]

    def hit(self, timestamp: int) -> None:
        if self.time_hits[-1][0] == timestamp:
            self.time_hits[-1][1] += 1
        else:
            self.time_hits.append([timestamp, self.time_hits[-1][1] + 1])

    def getHits(self, timestamp: int) -> int:
        end_count = self.getTotalHits(timestamp)
        start_count = self.getTotalHits(timestamp-300)

        return end_count - start_count

    def getTotalHits(self, timestamp):
        low = 0
        high = len(self.time_hits)
        while low < high:
            mid = (low + high) // 2
            if self.time_hits[mid][0] > timestamp:
                high = mid - 1
            elif self.time_hits[mid][0] < timestamp:
                low = mid + 1
            else:
                low = high = mid

        count = 0
        if low == len(self.time_hits) or low > 0 and self.time_hits[low][0] > timestamp:
            count = self.time_hits[low-1][1]
        else:
            count = self.time_hits[low][1]

        return count

# deque

from collections import deque
class HitCounter:

    def __init__(self):
        self.time_hits = deque() # [timestamp, totalhits]
        self.prev_count = 0

    def hit(self, timestamp: int) -> None:
        if self.time_hits and self.time_hits[-1][0] == timestamp:
            self.time_hits[-1][1] += 1
        else:
            entry = [timestamp, (self.time_hits[-1][1] if self.time_hits else self.prev_count) + 1]
            self.time_hits.append(entry)

    def getHits(self, timestamp: int) -> int:
        while self.time_hits and self.time_hits[0][0] <= timestamp - 300:
            _, self.prev_count = self.time_hits.popleft()

        return (self.time_hits[-1][1] - self.prev_count) if self.time_hits else 0

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
