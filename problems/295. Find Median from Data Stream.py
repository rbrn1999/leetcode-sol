# link: https://leetcode.com/problems/find-median-from-data-stream/
# solution reference: https://youtu.be/itmhHWaHupI
import heapq
class MedianFinder:

    def __init__(self):
        self.maxHeap = [] # smaller half of nums
        self.minHeap = [] # larger half of nums

    def addNum(self, num: int) -> None:
        if self.maxHeap and -self.maxHeap[0] > num:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        # balance size of two heaps
        if len(self.minHeap) > len(self.maxHeap) + 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        elif len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.minHeap) < len(self.maxHeap):
            return -self.maxHeap[0]
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2

# binary search solution
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