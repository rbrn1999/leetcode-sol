# link: https://leetcode.com/problems/find-median-from-data-stream/
# solution reference: https://youtu.be/itmhHWaHupI
import heapq
class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1*num)
        if (self.small and self.large) and (-1 * self.small[0]) > self.large[0]:
            heapq.heappush(self.large, -1 * heapq.heappop(self.small))
            
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -1 * heapq.heappop(self.small))
            
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -1 * heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2

# import bisect
# class MedianFinder:

#     def __init__(self):
#         self.arr = []

#     def addNum(self, num: int) -> None:
#         ind = bisect.bisect(self.arr, num)
#         self.arr.insert(ind, num)

#     def findMedian(self) -> float:
#         n = len(self.arr)
#         if n % 2:
#             return self.arr[n//2]
#         else:
#             return (self.arr[n//2-1] + self.arr[n//2]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()