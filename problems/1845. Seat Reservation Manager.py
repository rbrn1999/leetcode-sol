# link: https://leetcode.com/problems/seat-reservation-manager/
import heapq

class SeatManager:

    def __init__(self, n: int):
        self.heap = []
        self.p = 1 # seats from p~n are available and not been reserved or unreserved

    def reserve(self) -> int:
        if self.heap:
            return heapq.heappop(self.heap)
        else:
            seat = self.p
            self.p += 1
            return seat

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)