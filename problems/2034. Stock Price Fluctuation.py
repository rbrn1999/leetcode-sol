# link: https://leetcode.com/problems/stock-price-fluctuation/

import heapq
class StockPrice:

    def __init__(self):
        self.latest = 0
        self.timestamps = {}
        self.minHeap = []
        self.maxHeap = []

    def update(self, timestamp: int, price: int) -> None:
        self.latest = max(self.latest, timestamp)
        self.timestamps[timestamp] = price
        heapq.heappush(self.minHeap, (price, timestamp))
        heapq.heappush(self.maxHeap, (-price, timestamp))

    def current(self) -> int:
        return self.timestamps[self.latest]

    def maximum(self) -> int:
        while -self.maxHeap[0][0] != self.timestamps[self.maxHeap[0][1]]:
            heapq.heappop(self.maxHeap)
        return -self.maxHeap[0][0]

    def minimum(self) -> int:
        while self.minHeap[0][0] != self.timestamps[self.minHeap[0][1]]:
            heapq.heappop(self.minHeap)
        return self.minHeap[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()