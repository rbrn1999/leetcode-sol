# link: https://leetcode.com/problems/kth-largest-element-in-an-array/
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # max heap: time complexity: O(n+klog(n))
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)
        for _ in range(k-1):
            heapq.heappop(maxHeap)
        return -heapq.heappop(maxHeap)

        # quick select: time complexity: average O(n), worst O(n^2)
        # k -= 1 # convert to index
        # def quickSelect(start=0, end=len(nums)-1):
        #     pivot = nums[end]
        #     p = start
        #     for i in range(start, end):
        #         if nums[i] >= pivot:
        #             nums[i], nums[p] = nums[p], nums[i]
        #             p += 1
        #     nums[end], nums[p] = nums[p], nums[end]
        #     if p == k:
        #         return nums[p]
        #     elif p > k:
        #         return quickSelect(start, p-1)
        #     else:
        #         return quickSelect(p+1, end)

        # return quickSelect()

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        pq = nums[:k]
        heapq.heapify(pq)
        for num in nums[k:]:
            heapq.heappush(pq, num)
            heapq.heappop(pq)
        return pq[0]
